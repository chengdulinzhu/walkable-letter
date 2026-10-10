from PIL import Image, ImageDraw

p = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\characters\player_cat.png"
im = Image.open(p).convert("RGBA")
w, h = im.size

seeds = []
for x in range(0, w, 4):
    seeds.append((x, 0)); seeds.append((x, h - 1))
for y in range(0, h, 4):
    seeds.append((0, y)); seeds.append((w - 1, y))

filled = 0
for s in seeds:
    pxl = im.getpixel(s)
    if pxl[0] > 230 and pxl[1] > 230 and pxl[2] > 230:
        ImageDraw.floodfill(im, s, (255, 0, 255, 255), thresh=25)
        filled += 1

data = im.load()
removed = 0
for y in range(h):
    for x in range(w):
        if data[x, y] == (255, 0, 255, 255):
            data[x, y] = (0, 0, 0, 0)
            removed += 1
im.save(p)
print("seeds tried:", filled, "removed px:", removed)

shot = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\_shots\cat_sheet_labeled.png"
canvas = Image.new("RGBA", (4*256+30, 4*256+30), (200, 30, 30, 255))
d = ImageDraw.Draw(canvas)
for i in range(16):
    rr, cc = i // 4, i % 4
    cell = im.crop((cc*256, rr*256, cc*256+256, rr*256+256))
    canvas.paste(cell, (cc*256+15, rr*256+15), cell)
    d.text((cc*256+20, rr*256+20), str(i), fill=(255, 80, 80, 255))
canvas.save(shot)
print("labeled:", shot)
