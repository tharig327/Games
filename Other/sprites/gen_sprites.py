from PIL import Image, ImageDraw
import os

OUT = "/home/user/Games/Other/sprites"
os.makedirs(OUT, exist_ok=True)

SKIN = (252, 196, 140, 255)
HAIR = (74, 47, 32, 255)
MUSTACHE = (58, 36, 24, 255)
SHOE = (91, 58, 33, 255)
GLOVE = (255, 255, 255, 255)
BUTTON = (255, 215, 0, 255)
EYE = (20, 20, 20, 255)
OUTLINE = (18, 14, 16, 255)

def shade(c, f=0.7):
    return (int(c[0]*f), int(c[1]*f), int(c[2]*f), 255)

def rect(draw, x, y, w, h, color):
    draw.rectangle([x, y, x+w-1, y+h-1], fill=color)

def draw_small(shirt, overalls, pose):
    W, H = 16, 23
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(img)
    cap_brim = shade(shirt)

    # cap dome
    rect(d, 5, 0, 6, 1, shirt)
    rect(d, 3, 1, 10, 1, shirt)
    rect(d, 2, 2, 11, 1, shirt)
    rect(d, 1, 3, 12, 1, shirt)
    rect(d, 0, 4, 13, 1, shirt)
    # brim
    rect(d, 12, 4, 4, 1, cap_brim)
    rect(d, 6, 5, 10, 1, cap_brim)

    # hair peeking at back
    rect(d, 0, 5, 2, 2, HAIR)

    # face
    rect(d, 1, 6, 13, 2, SKIN)
    rect(d, 1, 8, 13, 1, SKIN)
    rect(d, 13, 7, 3, 2, SKIN)  # nose bump, protrudes further
    # eye
    rect(d, 8, 6, 2, 2, EYE)
    # mustache + lower face
    rect(d, 1, 9, 5, 1, SKIN)
    rect(d, 6, 9, 7, 2, MUSTACHE)
    rect(d, 1, 10, 5, 1, SKIN)

    # collar/shirt top
    rect(d, 1, 11, 13, 1, shirt)
    # shoulders + arms
    rect(d, 0, 12, 16, 2, shirt)
    rect(d, 0, 12, 2, 3, GLOVE)
    rect(d, 14, 12, 2, 3, GLOVE)

    # overalls torso
    rect(d, 2, 14, 12, 5, overalls)
    rect(d, 5, 15, 1, 1, BUTTON)
    rect(d, 10, 15, 1, 1, BUTTON)

    if pose == "idle":
        rect(d, 3, 19, 4, 2, overalls)
        rect(d, 9, 19, 4, 2, overalls)
        rect(d, 2, 21, 5, 2, SHOE)
        rect(d, 9, 21, 5, 2, SHOE)
    elif pose == "run1":
        rect(d, 2, 19, 4, 2, overalls)
        rect(d, 9, 19, 4, 1, overalls)
        rect(d, 1, 21, 5, 2, SHOE)
        rect(d, 9, 20, 6, 3, SHOE)
    elif pose == "run2":
        rect(d, 3, 19, 4, 1, overalls)
        rect(d, 9, 19, 4, 2, overalls)
        rect(d, 2, 20, 6, 3, SHOE)
        rect(d, 10, 21, 5, 2, SHOE)
    elif pose == "jump":
        rect(d, 2, 18, 5, 3, overalls)
        rect(d, 9, 18, 5, 3, overalls)
        rect(d, 1, 20, 6, 3, SHOE)
        rect(d, 9, 20, 6, 3, SHOE)

    return img

def draw_big(shirt, overalls, pose):
    W, H = 16, 31
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(img)
    cap_brim = shade(shirt)

    rect(d, 5, 0, 6, 1, shirt)
    rect(d, 3, 1, 10, 1, shirt)
    rect(d, 2, 2, 11, 1, shirt)
    rect(d, 1, 3, 12, 1, shirt)
    rect(d, 0, 4, 13, 1, shirt)
    rect(d, 12, 4, 4, 1, cap_brim)
    rect(d, 6, 5, 10, 1, cap_brim)
    rect(d, 0, 5, 2, 2, HAIR)

    rect(d, 1, 6, 13, 2, SKIN)
    rect(d, 1, 8, 13, 1, SKIN)
    rect(d, 13, 7, 3, 2, SKIN)
    rect(d, 8, 6, 2, 2, EYE)
    rect(d, 1, 9, 5, 1, SKIN)
    rect(d, 6, 9, 7, 2, MUSTACHE)
    rect(d, 1, 10, 5, 1, SKIN)

    rect(d, 1, 11, 13, 1, shirt)
    rect(d, 0, 12, 16, 3, shirt)
    rect(d, 0, 12, 2, 4, GLOVE)
    rect(d, 14, 12, 2, 4, GLOVE)

    rect(d, 2, 15, 12, 12, overalls)
    rect(d, 5, 16, 1, 1, BUTTON)
    rect(d, 10, 16, 1, 1, BUTTON)

    if pose == "idle":
        rect(d, 3, 27, 4, 2, overalls)
        rect(d, 9, 27, 4, 2, overalls)
        rect(d, 2, 29, 5, 2, SHOE)
        rect(d, 9, 29, 5, 2, SHOE)
    elif pose == "run1":
        rect(d, 2, 27, 4, 2, overalls)
        rect(d, 9, 27, 4, 1, overalls)
        rect(d, 1, 29, 5, 2, SHOE)
        rect(d, 9, 28, 6, 3, SHOE)
    elif pose == "run2":
        rect(d, 3, 27, 4, 1, overalls)
        rect(d, 9, 27, 4, 2, overalls)
        rect(d, 2, 28, 6, 3, SHOE)
        rect(d, 10, 29, 5, 2, SHOE)
    elif pose == "jump":
        rect(d, 2, 26, 5, 3, overalls)
        rect(d, 9, 26, 5, 3, overalls)
        rect(d, 1, 28, 6, 3, SHOE)
        rect(d, 9, 28, 6, 3, SHOE)

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

CHARACTERS = {
    "mario": {"shirt": (230, 57, 70, 255)},
    "luigi": {"shirt": (26, 143, 90, 255)},
}
FORMS = {
    "small": {"overalls": (39, 70, 144, 255), "big": False},
    "big": {"overalls": (39, 70, 144, 255), "big": True},
    "fire": {"overalls": (255, 255, 255, 255), "big": True},
    "bounce": {"overalls": (28, 143, 143, 255), "big": True},
}
POSES = ["idle", "run1", "run2", "jump"]

for cname, cinfo in CHARACTERS.items():
    for fname, finfo in FORMS.items():
        shirt = cinfo["shirt"]
        overalls = finfo["overalls"]
        # bounce form uses gold shirt regardless of character (existing convention)
        this_shirt = (247, 181, 0, 255) if fname == "bounce" else shirt
        for pose in POSES:
            if finfo["big"]:
                img = draw_big(this_shirt, overalls, pose)
            else:
                img = draw_small(this_shirt, overalls, pose)
            img = add_outline(img)
            fname_out = f"{OUT}/{cname}_{fname}_{pose}.png"
            img.save(fname_out)

print("done, generated", len(CHARACTERS)*len(FORMS)*len(POSES), "sprites")
