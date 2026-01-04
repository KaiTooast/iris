"""
SwinIR: Image Restoration Using Swin Transformer
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from timm.models.layers import DropPath, to_2tuple, trunc_normal_


class Mlp(nn.Module):
    def __init__(self, in_features, hidden_features=None, out_features=None, act_layer=nn.GELU, drop=0.):
        super().__init__()
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features
        self.fc1 = nn.Linear(in_features, hidden_features)
        self.act = act_layer()
        self.fc2 = nn.Linear(hidden_features, out_features)
        self.drop = nn.Dropout(drop)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.drop(x)
        return x


class WindowAttention(nn.Module):
    def __init__(self, dim, window_size, num_heads, qkv_bias=True, attn_drop=0., proj_drop=0.):
        super().__init__()
        self.dim = dim
        self.window_size = window_size
        self.num_heads = num_heads
        head_dim = dim // num_heads
        self.scale = head_dim ** -0.5

        self.relative_position_bias_table = nn.Parameter(
            torch.zeros((2 * window_size[0] - 1) * (2 * window_size[1] - 1), num_heads))

        coords_h = torch.arange(self.window_size[0])
        coords_w = torch.arange(self.window_size[1])
        coords = torch.stack(torch.meshgrid([coords_h, coords_w]))
        coords_flatten = torch.flatten(coords, 1)
        relative_coords = coords_flatten[:, :, None] - coords_flatten[:, None, :]
        relative_coords = relative_coords.permute(1, 2, 0).contiguous()
        relative_coords[:, :, 0] += self.window_size[0] - 1
        relative_coords[:, :, 1] += self.window_size[1] - 1
        relative_coords[:, :, 0] *= 2 * self.window_size[1] - 1
        relative_position_index = relative_coords.sum(-1)
        self.register_buffer("relative_position_index", relative_position_index)

        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)
        self.attn_drop = nn.Dropout(attn_drop)
        self.proj = nn.Linear(dim, dim)
        self.proj_drop = nn.Dropout(proj_drop)

        trunc_normal_(self.relative_position_bias_table, std=.02)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        B_, N, C = x.shape
        qkv = self.qkv(x).reshape(B_, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]

        q = q * self.scale
        attn = (q @ k.transpose(-2, -1))

        relative_position_bias = self.relative_position_bias_table[self.relative_position_index.view(-1)].view(
            self.window_size[0] * self.window_size[1], self.window_size[0] * self.window_size[1], -1)
        relative_position_bias = relative_position_bias.permute(2, 0, 1).contiguous()
        attn = attn + relative_position_bias.unsqueeze(0)

        attn = self.softmax(attn)
        attn = self.attn_drop(attn)

        x = (attn @ v).transpose(1, 2).reshape(B_, N, C)
        x = self.proj(x)
        x = self.proj_drop(x)
        return x


class SwinIR(nn.Module):
    def __init__(self, upscale=4, in_chans=3, img_size=64, window_size=8,
                 img_range=1., depths=[6, 6, 6, 6], embed_dim=96, num_heads=[6, 6, 6, 6],
                 mlp_ratio=2., upsampler='pixelshuffle', resi_connection='1conv'):
        super(SwinIR, self).__init__()
        
        self.window_size = window_size
        self.upscale = upscale
        
        # Shallow feature extraction
        self.conv_first = nn.Conv2d(in_chans, embed_dim, 3, 1, 1)
        
        # Deep feature extraction (simplified for this implementation)
        self.norm = nn.LayerNorm(embed_dim)
        
        # Reconstruction
        if upsampler == 'pixelshuffle':
            self.conv_before_upsample = nn.Sequential(
                nn.Conv2d(embed_dim, embed_dim, 3, 1, 1),
                nn.LeakyReLU(inplace=True))
            self.upsample = nn.Sequential(
                nn.Conv2d(embed_dim, (upscale ** 2) * in_chans, 3, 1, 1),
                nn.PixelShuffle(upscale))
        elif upsampler == 'nearest+conv':
            self.conv_before_upsample = nn.Sequential(
                nn.Conv2d(embed_dim, embed_dim, 3, 1, 1),
                nn.LeakyReLU(inplace=True))
            self.conv_up1 = nn.Conv2d(embed_dim, embed_dim, 3, 1, 1)
            if upscale == 4:
                self.conv_up2 = nn.Conv2d(embed_dim, embed_dim, 3, 1, 1)
            self.conv_hr = nn.Conv2d(embed_dim, embed_dim, 3, 1, 1)
            self.conv_last = nn.Conv2d(embed_dim, in_chans, 3, 1, 1)
            self.lrelu = nn.LeakyReLU(negative_slope=0.2, inplace=True)
        
        self.upsampler = upsampler

    def forward(self, x):
        x = self.conv_first(x)
        x = self.conv_before_upsample(x)
        
        if self.upsampler == 'pixelshuffle':
            x = self.upsample(x)
        elif self.upsampler == 'nearest+conv':
            x = self.lrelu(self.conv_up1(F.interpolate(x, scale_factor=2, mode='nearest')))
            if self.upscale == 4:
                x = self.lrelu(self.conv_up2(F.interpolate(x, scale_factor=2, mode='nearest')))
            x = self.conv_last(self.lrelu(self.conv_hr(x)))
        
        return x
