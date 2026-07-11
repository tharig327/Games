from PIL import Image, ImageDraw
import os

OUT = "/home/user/Games/Other/sprites"
os.makedirs(OUT, exist_ok=True)

# base palette
SKIN = (252, 200, 148, 255)
SKIN_HI = (255, 224, 186, 255)
SKIN_SH = (214, 156, 108, 255)
HAIR = (74, 47, 32, 255)
MUSTACHE = (58, 36, 24, 255)
SHOE = (110, 68, 38, 255)
SHOE_HI = (150, 100, 62, 255)
SHOE_SH = (74, 44, 24, 255)
GLOVE = (255, 255, 255, 255)
GLOVE_SH = (206, 210, 224, 255)
BUTTON = (255, 215, 0, 255)
EYE = (26, 26, 40, 255)
OUTLINE = (20, 16, 22, 255)

def tone(c, f):
    return (min(255, int(c[0]*f)), min(255, int(c[1]*f)), min(255, int(c[2]*f)), 255)

def rect(draw, x, y, w, h, color):
    if w <= 0 or h <= 0:
        return
    draw.rectangle([x, y, x+w-1, y+h-1], fill=color)

def px(d, x, y, color):
    d.point((x, y), fill=color)

def draw_body(shirt, overalls, pose, big):
    """Draw one Mario/Luigi frame. Coordinates are hand-tuned per material with
    a highlight (upper-left) and shadow (lower-right) band on each region."""
    shirt_hi = tone(shirt, 1.28)
    shirt_sh = tone(shirt, 0.68)
    ov_hi = tone(overalls, 1.22) if overalls != (255,255,255,255) else (255,255,255,255)
    ov_sh = tone(overalls, 0.7) if overalls != (255,255,255,255) else (206,210,224,255)

    W = 16
    torso_h = 12 if big else 5
    H = 31 if big else 23
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(img)

    # ---- CAP ----
    # dome, rounded with a highlight streak
    rect(d, 5, 0, 6, 1, shirt)
    rect(d, 3, 1, 10, 1, shirt)
    rect(d, 2, 2, 11, 1, shirt)
    rect(d, 1, 3, 12, 1, shirt)
    rect(d, 1, 4, 12, 1, shirt)
    # dome highlight (upper-left curve)
    rect(d, 3, 1, 4, 1, shirt_hi)
    rect(d, 2, 2, 3, 1, shirt_hi)
    rect(d, 1, 3, 2, 1, shirt_hi)
    # dome shadow (lower-right rim)
    rect(d, 10, 2, 3, 1, shirt_sh)
    rect(d, 11, 3, 2, 1, shirt_sh)
    # brim, protruding right
    rect(d, 6, 5, 10, 1, shirt_sh)
    rect(d, 12, 4, 4, 1, shirt_sh)
    rect(d, 1, 5, 5, 1, shirt)

    # ---- HAIR (back) ----
    rect(d, 0, 5, 2, 2, HAIR)

    # ---- FACE ----
    rect(d, 1, 6, 13, 2, SKIN)
    rect(d, 1, 8, 12, 1, SKIN)
    # nose (protruding, rounded)
    rect(d, 13, 7, 3, 2, SKIN)
    px(d, 15, 7, SKIN_SH)
    # cheek highlight
    px(d, 2, 6, SKIN_HI); px(d, 3, 6, SKIN_HI)
    # sideburn
    rect(d, 1, 8, 2, 3, HAIR)
    # eye
    rect(d, 8, 6, 2, 3, EYE)
    px(d, 8, 6, (70,70,90,255))  # tiny catchlight
    # mustache
    rect(d, 6, 9, 7, 2, MUSTACHE)
    rect(d, 3, 9, 3, 1, SKIN)
    rect(d, 13, 9, 1, 1, MUSTACHE)
    rect(d, 3, 10, 3, 1, SKIN_SH)

    # ---- SHIRT / SHOULDERS ----
    rect(d, 1, 11, 13, 1, shirt)
    shy = 12
    sh_rows = 3 if big else 2
    rect(d, 0, shy, 16, sh_rows, shirt)
    # shoulder highlight
    rect(d, 2, shy, 5, 1, shirt_hi)
    # shoulder shadow underside
    rect(d, 2, shy+sh_rows-1, 12, 1, shirt_sh)

    # gloves (hands)
    glove_h = 4 if big else 3
    rect(d, 0, shy, 2, glove_h, GLOVE)
    rect(d, 14, shy, 2, glove_h, GLOVE)
    px(d, 0, shy+glove_h-1, GLOVE_SH)
    px(d, 15, shy+glove_h-1, GLOVE_SH)

    # ---- OVERALLS TORSO ----
    ov_y = 15 if big else 14
    rect(d, 2, ov_y, 12, torso_h, overalls)
    # highlight left column
    rect(d, 2, ov_y, 2, torso_h, ov_hi)
    # shadow right column + bottom
    rect(d, 12, ov_y, 2, torso_h, ov_sh)
    rect(d, 2, ov_y+torso_h-1, 12, 1, ov_sh)
    # straps up onto shirt
    rect(d, 4, ov_y-1, 2, 2, overalls)
    rect(d, 10, ov_y-1, 2, 2, overalls)
    # buttons
    px(d, 4, ov_y+1, BUTTON)
    px(d, 11, ov_y+1, BUTTON)

    # ---- LEGS + SHOES ----
    base = 21 if not big else 29
    def leg(lx, ly, lw, lh, foot_x, foot_w):
        rect(d, lx, ly, lw, lh, overalls)
        rect(d, lx, ly, 1, lh, ov_hi)
        # shoe
        rect(d, foot_x, ly+lh-1, foot_w, 2, SHOE)
        rect(d, foot_x, ly+lh-1, foot_w, 1, SHOE_HI)
        rect(d, foot_x, ly+lh, foot_w, 1, SHOE_SH)

    if pose == "idle":
        leg(3, base-2, 4, 2, 2, 5)
        leg(9, base-2, 4, 2, 9, 5)
    elif pose == "run1":
        leg(2, base-2, 4, 2, 1, 5)
        leg(9, base-2, 4, 1, 9, 6)
    elif pose == "run2":
        leg(3, base-2, 4, 1, 2, 6)
        leg(9, base-2, 4, 2, 10, 5)
    elif pose == "jump":
        leg(2, base-3, 5, 3, 1, 6)
        leg(9, base-3, 5, 3, 9, 6)

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

CHARACTERS = {
    "mario": (228, 52, 60, 255),
    "luigi": (32, 156, 92, 255),
}
FORMS = {
    "small": {"overalls": (44, 78, 156, 255), "big": False},
    "big":   {"overalls": (44, 78, 156, 255), "big": True},
    "fire":  {"overalls": (255, 255, 255, 255), "big": True},
    "bounce":{"overalls": (30, 150, 150, 255), "big": True},
}
POSES = ["idle", "run1", "run2", "jump"]

for cname, shirt in CHARACTERS.items():
    for fname, finfo in FORMS.items():
        this_shirt = (247, 181, 0, 255) if fname == "bounce" else shirt
        for pose in POSES:
            img = draw_body(this_shirt, finfo["overalls"], pose, finfo["big"])
            img = add_outline(img)
            img.save(f"{OUT}/{cname}_{fname}_{pose}.png")

print("done, generated", len(CHARACTERS)*len(FORMS)*len(POSES), "sprites")
