from PIL import Image
import os

# 打开原始礼物盒图
img_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box.png"
img = Image.open(img_path).convert("RGBA")

# 只把礼物盒内部的透明像素填上白色，外面保持透明
# 先裁剪到礼物盒的实际范围
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# 把透明像素（alpha < 128）的地方填上白色，但保持透明度不变
# 这样礼物盒内部抠漏的地方就有白底了，外面还是透明的
data = img.getdata()
new_data = []
for item in data:
    r, g, b, a = item
    if a < 128:
        # 透明的地方，填上白色，但保持低透明度（这样外面还是透明的）
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
img.putdata(new_data)

# 保存
out_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box_fixed.png"
img.save(out_path)
print(f"Saved to {out_path}")
print(f"Size: {img.size}")
