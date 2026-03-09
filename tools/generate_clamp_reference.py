#!/usr/bin/env python3
"""
Generate a colorized reference image for RM_CLAMP comparison.
Test pattern: 16 vertical LORES color bars (colors 1-16) + text lines.
Canonical source: assets/applesoft_color_test.bas
Uses Apple IIgs LORES palette sRGB values. Output saved to assets/clamp_reference_expected.png
Requires: pip install Pillow
"""
import os

# Apple II LORES palette - sRGB values matching estimated_appearance
# Order: black, magenta, darkblue, purple, darkgreen, gray1, mediumblue, lightblue,
#        brown, orange, gray2, pink, green, yellow, aqua, white
PALETTE = [
    (0x00, 0x00, 0x00),  # 0 black
    (0x9d, 0x09, 0x66),  # 1 magenta (vibrant red-magenta)
    (0x2a, 0x2a, 0xe5),  # 2 darkblue
    (0xc7, 0x34, 0xff),  # 3 purple
    (0x00, 0x80, 0x00),  # 4 darkgreen
    (0x80, 0x80, 0x80),  # 5 gray1
    (0x0d, 0xa1, 0xff),  # 6 mediumblue
    (0xaa, 0xaa, 0xff),  # 7 lightblue
    (0x55, 0x55, 0x00),  # 8 brown
    (0xf2, 0x5e, 0x00),  # 9 orange
    (0xC0, 0xC0, 0xC0),  # 10 gray2
    (0xff, 0x89, 0xe5),  # 11 pink
    (0x38, 0xcb, 0x00),  # 12 green
    (0xd5, 0xd5, 0x1a),  # 13 yellow
    (0x62, 0xf6, 0x99),  # 14 aqua
    (0xff, 0xff, 0xff),  # 15 white
]

# Layout: 640x480 typical, 16 bars + text area
W, H = 640, 480
BAR_HEIGHT = 360  # ~3/4 for color bars
TEXT_Y = 380
BAR_WIDTH = W // 16  # 40 px each


def make_rgb_grid():
    """Build WxH RGB grid: 16 bars + text area."""
    grid = [[(0, 0, 0)] * W for _ in range(H)]
    # 16 vertical color bars (colors 0-15)
    for i in range(16):
        c = PALETTE[i]
        x0, x1 = i * BAR_WIDTH, (i + 1) * BAR_WIDTH
        for y in range(BAR_HEIGHT):
            for x in range(x0, min(x1, W)):
                grid[y][x] = c
    # Simple block digits for "0123456789111111", "012345", "]"
    # 5x7 pixel font (simplified blocks)
    def block_char(grid, x0, y0, w, h, color):
        for dy in range(h):
            for dx in range(w):
                if 0 <= y0 + dy < H and 0 <= x0 + dx < W:
                    grid[y0 + dy][x0 + dx] = color
    cw, ch = 10, 14
    white = (255, 255, 255)
    # Line 1: 0123456789111111
    for i in range(16):
        block_char(grid, 8 + i * cw, TEXT_Y, cw - 1, ch, white)
    # Line 2: ] at left, 012345 shifted right
    block_char(grid, 8, TEXT_Y + ch + 6, cw - 1, ch, white)  # ]
    for i in range(6):
        block_char(grid, 8 + (2 + i) * cw, TEXT_Y + ch + 6, cw - 1, ch, white)  # 012345
    return grid


def write_ppm(grid, path):
    """Write PPM (no deps)."""
    with open(path, "wb") as f:
        f.write(f"P6\n{W} {H}\n255\n".encode())
        for row in grid:
            for r, g, b in row:
                f.write(bytes((r, g, b)))


def main():
    os.makedirs("assets", exist_ok=True)
    grid = make_rgb_grid()

    # Try PNG via Pillow
    try:
        from PIL import Image
        img = Image.new("RGB", (W, H))
        for y in range(H):
            for x in range(W):
                img.putpixel((x, y), grid[y][x])
        out = "assets/clamp_reference_expected.png"
        img.save(out)
    except ImportError:
        out = "assets/clamp_reference_expected.ppm"
        write_ppm(grid, out)
        print("(Install Pillow for PNG output: pip install Pillow)")

    print(f"Saved {out}")
    return 0


if __name__ == "__main__":
    exit(main())
