from PIL import Image
import os

# 打开原始礼物盒图
img_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box.png"
img = Image.open(img_path).convert("RGBA")

# 去掉白边：把接近白色的像素变成透明
data = img.getdata()
new_data = []
for item in data:
    # 白色（255,255,255）附近的像素变成透明
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
img.putdata(new_data)

# 裁剪透明边缘
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# 垫白底：在礼物盒下面加一个白色背景
# 创建一个比礼物盒大一点的白底
w, h = img.size
white_bg = Image.new("RGBA", (w + 20, h + 20), (255, 255, 255, 255))
white_bg.paste(img, (10, 10), img)

# 保存
out_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box_fixed.png"
white_bg.save(out_path)
print(f"Saved to {out_path}")
print(f"Size: {white_bg.size}")
