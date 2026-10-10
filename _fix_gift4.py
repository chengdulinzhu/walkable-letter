from PIL import Image
import os

# 打开原始礼物盒图
img_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box.png"
img = Image.open(img_path).convert("RGBA")
w, h = img.size
pixels = img.load()

# 简单粗暴的方法：把最外层一圈的白色像素变成透明
# 然后往内缩，直到碰到非白色的像素
def is_white(x, y):
    r, g, b, a = pixels[x, y]
    return r > 240 and g > 240 and b > 240

# 从边缘开始，一圈一圈地把白色变透明
left, right, top, bottom = 0, w-1, 0, h-1

# 左边
while left < w and is_white(left, h//2):
    for y in range(h):
        pixels[left, y] = (255, 255, 255, 0)
    left += 1

# 右边
while right >= 0 and is_white(right, h//2):
    for y in range(h):
        pixels[right, y] = (255, 255, 255, 0)
    right -= 1

# 上边
while top < h and is_white(w//2, top):
    for x in range(w):
        pixels[x, top] = (255, 255, 255, 0)
    top += 1

# 下边
while bottom >= 0 and is_white(w//2, bottom):
    for x in range(w):
        pixels[x, bottom] = (255, 255, 255, 0)
    bottom -= 1

# 裁剪
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# 保存
out_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box_fixed.png"
img.save(out_path)
print(f"Saved to {out_path}")
print(f"Size: {img.size}")
