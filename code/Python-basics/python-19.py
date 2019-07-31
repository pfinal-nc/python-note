# 常用模块
from PIL import Image,ImageFilter

# 图像库
im = Image.open('./1.jpg')
# 获得大小
w,h = im.size
print(w,h)

# 缩放到50%
im.thumbnail((w//2,h//2))
print(w//2,h//2)
# 保存
# im.save('2.jpg','jpeg')

# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('2.jpg','jpeg')
