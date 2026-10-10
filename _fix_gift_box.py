from PIL import Image, ImageDraw

# 打开礼物盒图
img = Image.open('assets/memory-objects/gift_box_fixed.png')
width, height = img.size

# 在中间画一个白色的矩形，大小比图案小一点
# 左右各留 60px，上下各留 50px
left = 60
top = 50
right = width - 60
bottom = height - 50

# 创建一个可以画图的对象
draw = ImageDraw.Draw(img)

# 画白色的矩形（不透明）
draw.rectangle([left, top, right, bottom], fill=(255, 255, 255, 255))

# 保存为新的图
img.save('assets/memory-objects/gift_box_white.png')
print('Done: gift_box_white.png')
