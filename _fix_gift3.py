from PIL import Image
import os

# 打开原始礼物盒图（带白边的）
img_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box.png"
img = Image.open(img_path).convert("RGBA")

# 从边缘开始，把外围的白色背景抠掉（变成透明）
# 用洪水填充的方法：从四个角开始，把连通的白色像素变成透明
import numpy as np
from collections import deque

data = np.array(img)
h, w = data.shape[:2]

# 白色的阈值
def is_white(r, g, b):
    return r > 240 and g > 240 and b > 240

# 标记哪些像素是外围白色（需要变透明）
visited = np.zeros((h, w), dtype=bool)
queue = deque()

# 从四个角开始
for x, y in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]:
    if is_white(data[y, x, 0], data[y, x, 1], data[y, x, 2]):
        queue.append((x, y))
        visited[y, x] = True

# 洪水填充
while queue:
    x, y = queue.popleft()
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx]:
            if is_white(data[ny, nx, 0], data[ny, nx, 1], data[ny, nx, 2]):
                visited[ny, nx] = True
                queue.append((nx, ny))

# 把外围白色变成透明
data[visited, 3] = 0

# 裁剪透明边缘
non_transparent = np.where(data[..., 3] > 0)
if len(non_transparent[0]) > 0:
    y_min, y_max = non_transparent[0].min(), non_transparent[0].max()
    x_min, x_max = non_transparent[1].min(), non_transparent[1].max()
    data = data[y_min:y_max+1, x_min:x_max+1]

# 保存
out_img = Image.fromarray(data)
out_path = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\memory-objects\gift_box_fixed.png"
out_img.save(out_path)
print(f"Saved to {out_path}")
print(f"Size: {out_img.size}")
