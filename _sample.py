from PIL import Image
p = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets\characters\player_cat.png"
im = Image.open(p).convert("RGBA")
print("size:", im.size)
# 背景采样点（应在格角落/格间隙）
for xy in [(0,0),(255,0),(0,255),(255,255),(128,0),(0,128),(256,256),(511,0),(0,511),
           (128,128),(100,100),(200,200),(60,160),(180,60),(384,128)]:
    print(xy, im.getpixel(xy))
