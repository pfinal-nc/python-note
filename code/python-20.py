# 生成验证码
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

# 生成随机数字

def randChar():
    return chr(random.randint(65,90))

# 生成随机颜色
def randColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 随机颜色
def randColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# 验证码宽高
width = 60*4
height=60
image = Image.new('RGB',(width,height),(255,255,255))

# 创建字体库
font = ImageFont.truetype('Arial.ttf',36)
# 创建Draw对象
draw = ImageDraw.Draw(image)


for x in range(width):
    for j in range(height):
        draw.point((x,j),fill=randColor())   # 画点

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')