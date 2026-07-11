from PIL import Image, ImageDraw
import os

OUT = "/home/user/Games/Other/sprites"
os.makedirs(OUT, exist_ok=True)

GREEN = (66, 176, 58, 255)
GREEN_HI = (110, 208, 96, 255)
GREEN_SH = (44, 132, 40, 255)
CREAM = (253, 246, 227, 255)
CREAM_SH = (222, 210, 180, 255)
SADDLE = (150, 66, 38, 255)
SADDLE_HI = (186, 96, 60, 255)
SPIKE = (228, 52, 60, 255)
SPIKE_HI = (250, 96, 104, 255)
EYE_W = (255, 255, 255, 255)
EYE_K = (26, 26, 40, 255)
SHOE = (240, 128, 32, 255)
SHOE_HI = (255, 168, 74, 255)
SHOE_SH = (196, 92, 18, 255)
OUTLINE = (20, 16, 22, 255)

def rect(draw, x, y, w, h, color):
    if w <= 0 or h <= 0:
        return
    draw.rectangle([x, y, x+w-1, y+h-1], fill=color)

def px(d, x, y, color):
    d.point((x, y), fill=color)

def draw_yoshi(pose):
    W, H = 34, 22
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(img)

    # ---- TAIL (curls up at back-left) ----
    rect(d, 0, 10, 3, 2, GREEN)
    rect(d, 0, 7, 2, 4, GREEN)
    rect(d, 1, 5, 2, 3, GREEN)
    px(d, 1, 5, GREEN_HI)

    # ---- LEGS + SHOES ----
    leg_positions = {
        "idle": [(4, 16, 4, 5), (17, 16, 4, 5)],
        "run1": [(3, 16, 4, 4), (18, 15, 4, 6)],
        "run2": [(4, 15, 4, 6), (17, 16, 4, 4)],
    }[pose]
    for (lx, ly, lw, lh) in leg_positions:
        rect(d, lx, ly, lw, lh, GREEN)
        rect(d, lx, ly, 1, lh, GREEN_HI)
        rect(d, lx+lw-1, ly, 1, lh, GREEN_SH)
        # shoe: highlight top, base, shadow bottom
        rect(d, lx-1, ly+lh-1, lw+2, 1, SHOE_HI)
        rect(d, lx-1, ly+lh,   lw+2, 1, SHOE)
        rect(d, lx-1, ly+lh+1, lw+2, 1, SHOE_SH)

    # ---- BODY (wide low blob) ----
    rect(d, 3, 8, 20, 8, GREEN)
    rect(d, 2, 10, 22, 5, GREEN)
    rect(d, 5, 6, 15, 3, GREEN)
    # top highlight arc
    rect(d, 6, 6, 11, 1, GREEN_HI)
    rect(d, 4, 8, 4, 1, GREEN_HI)
    # bottom / right shadow
    rect(d, 3, 14, 20, 1, GREEN_SH)
    rect(d, 21, 9, 2, 5, GREEN_SH)

    # ---- CREAM BELLY ----
    rect(d, 7, 10, 11, 5, CREAM)
    rect(d, 7, 14, 11, 1, CREAM_SH)
    rect(d, 16, 10, 2, 4, CREAM_SH)

    # ---- BACK SPIKES ----
    for sx in (6, 10, 14):
        rect(d, sx, 3, 2, 3, SPIKE)
        px(d, sx, 3, SPIKE_HI)

    # ---- SADDLE STRAP ----
    rect(d, 4, 7, 17, 2, SADDLE)
    rect(d, 4, 7, 17, 1, SADDLE_HI)

    # ---- HEAD + SNOUT (facing right) ----
    rect(d, 20, 0, 9, 8, GREEN)
    rect(d, 27, 3, 5, 4, GREEN)
    # head highlight (upper-left of head)
    rect(d, 21, 0, 4, 1, GREEN_HI)
    rect(d, 20, 1, 2, 2, GREEN_HI)
    # snout shadow underside
    rect(d, 27, 6, 5, 1, GREEN_SH)
    # lighter snout tip
    rect(d, 31, 4, 3, 3, CREAM)
    px(d, 31, 6, CREAM_SH)
    px(d, 32, 5, GREEN_SH)  # nostril

    # ---- EAR ----
    rect(d, 19, 0, 2, 3, GREEN)
    px(d, 19, 0, GREEN_HI)

    # ---- EYE ----
    rect(d, 24, 1, 3, 4, EYE_W)
    rect(d, 25, 2, 2, 2, EYE_K)
    px(d, 25, 2, (90,90,120,255))  # catchlight

    return img

def add_outline(img, color=OUTLINE):
    w, h = img.size
    a = img.split()[-1].load()
    outline = Image.new("RGBA", img.size, (0,0,0,0))
    o = outline.load()
    for y in range(h):
        for x in range(w):
            if a[x, y] == 0:
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < w and 0 <= ny < h and a[nx, ny] > 0:
                        o[x, y] = color
                        break
    return Image.alpha_composite(outline, img)

for pose in ("idle", "run1", "run2"):
    img = draw_yoshi(pose)
    img = add_outline(img)
    img.save(f"{OUT}/yoshi_{pose}.png")

print("done")
