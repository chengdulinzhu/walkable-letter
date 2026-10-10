from PIL import Image
import os
base = r"C:\Users\心竹\DoubaoWork\chats\2026-10-08\new-chat-1\walkable-letter\assets"
for sub, name in [("maps","map_classroom.png"),("characters","player_cat.png")]:
    p = os.path.join(base, sub, name)
    im = Image.open(p)
    print(name, im.size, im.mode)
