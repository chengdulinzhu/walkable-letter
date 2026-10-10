from PIL import Image, ImageDraw

# 从原始图重新抠白边，阈值加大 + 边缘半透明处理
src = r"C:\Users\心竹\AppData\Local\DoubaoWork\User Data\ClipboardTemp\b424611f-5bfc-4803-92d5-03c187d4fdd6.png"
dst = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\characters\player_cat.png"
im = Image.open(src).convert("RGBA")
w, h = im.size

# 1) 从边缘 flood fill，阈值 40 抠白底
seeds = []
for x in range(0, w, 3):
    seeds.append((x, 0)); seeds.append((x, h - 1))
for y in range(0, h, 3):
    seeds.append((0, y)); seeds.append((w - 1, y))
for s in seeds:
    pxl = im.getpixel(s)
    if pxl[0] > 225 and pxl[1] > 225 and pxl[2] > 225:
        ImageDraw.floodfill(im, s, (255, 0, 255, 255), thresh=40)

data = im.load()
removed = 0
for y in range(h):
    for x in range(w):
        p = data[x, y]
        if p == (255, 0, 255, 255):
            data[x, y] = (0, 0, 0, 0)
            removed += 1

# 2) 边缘清边：与透明像素相邻的"近白"像素，alpha 降到 80（去掉残留白边）
import collections
visited = [[False]*w for _ in range(h)]
def is_near_white(p):
    return p[3] > 0 and p[0] > 215 and p[1] > 215 and p[2] > 215
def is_transparent(p):
    return p[3] == 0

# 找所有与透明像素 8 邻接的近白像素
to_fix = []
for y in range(1, h-1):
    for x in range(1, w-1):
        p = data[x, y]
        if not is_near_white(p):
            continue
        for dy in (-1,0,1):
            for dx in (-1,0,1):
                if dx==0 and dy==0: continue
                if is_transparent(data[x+dx, y+dy]):
                    to_fix.append((x,y)); break
            else: continue
            break
for (x,y) in to_fix:
    p = data[x,y]
    data[x,y] = (p[0], p[1], p[2], 90)

im.save(dst)
print("removed:", removed, "edge softened:", len(to_fix))
