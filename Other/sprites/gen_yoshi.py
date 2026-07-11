from PIL import Image, ImageDraw
import os

OUT = "/home/user/Games/Other/sprites"
os.makedirs(OUT, exist_ok=True)

GREEN = (58, 168, 50, 255)
GREEN_DARK = (40, 128, 36, 255)
CREAM = (253, 246, 227, 255)
SADDLE = (163, 74, 42, 255)
SPIKE = (230, 57, 70, 255)
EYE_W = (255, 255, 255, 255)
EYE_K = (26, 26, 26, 255)
SHOE = (242, 129, 31, 255)
OUTLINE = (18, 14, 16, 255)

def rect(draw, x, y, w, h, color):
    draw.rectangle([x, y, x+w-1, y+h-1], fill=color)

def draw_yoshi(pose):
    W, H = 34, 22
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(img)

    # tail, curls up at the back (left side)
    rect(d, 0, 10, 3, 2, GREEN)
    rect(d, 0, 7, 2, 4, GREEN)
    rect(d, 1, 5, 2, 3, GREEN)

    # legs (vary per pose)
    leg_positions = {
        "idle": [(4, 16, 4, 5), (17, 16, 4, 5)],
        "run1": [(3, 16, 4, 4), (18, 15, 4, 6)],
        "run2": [(4, 15, 4, 6), (17, 16, 4, 4)],
    }[pose]
    for (lx, ly, lw, lh) in leg_positions:
        rect(d, lx, ly, lw, lh, GREEN)
        rect(d, lx-1, ly+lh-2, lw+2, 2, SHOE)

    # body, wide low blob
    rect(d, 3, 8, 20, 8, GREEN)
    rect(d, 2, 10, 22, 5, GREEN)
    rect(d, 5, 6, 15, 3, GREEN)

    # cream belly
    rect(d, 7, 10, 11, 5, CREAM)

    # back spikes
    for sx in (6, 10, 14):
        rect(d, sx, 3, 2, 3, SPIKE)

    # saddle strap
    rect(d, 4, 7, 17, 2, SADDLE)

    # head + big snout, facing right
    rect(d, 20, 0, 9, 8, GREEN)
    rect(d, 27, 3, 5, 4, GREEN)
    rect(d, 31, 4, 3, 3, CREAM)  # lighter snout tip
    rect(d, 32, 5, 1, 1, GREEN_DARK)  # nostril

    # ear
    rect(d, 19, 0, 2, 3, GREEN)

    # eye
    rect(d, 24, 1, 3, 3, EYE_W)
    rect(d, 25, 2, 2, 2, EYE_K)

    return img

def add_outline(img, color=OUTLINE):
    w, h = img.size
    alpha = img.split()[-1]
    a = alpha.load()
    outline = Image.new("RGBA", img.size, (0,0,0,0))
    o = outline.load()
    for y in range(h):
        for x in range(w):
            if a[x, y] == 0:
                neighbor = False
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < w and 0 <= ny < h and a[nx, ny] > 0:
                        neighbor = True
                        break
                if neighbor:
                    o[x, y] = color
    return Image.alpha_composite(outline, img)

for pose in ("idle", "run1", "run2"):
    img = draw_yoshi(pose)
    img = add_outline(img)
    img.save(f"{OUT}/yoshi_{pose}.png")

print("done")
