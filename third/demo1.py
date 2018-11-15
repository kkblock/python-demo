# -*- coding: utf-8 -*-
import chardet
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import psutil

'''
PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
下面是操作图像的一个例子
'''
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('/home/black/Pictures/a.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('/home/black/Pictures/a.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

'''
PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
'''


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象,这里要是报找不到,需要传字体的绝对路径
font = ImageFont.truetype('AppleGaramond.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

# 生成验证码结束


'''
chardet 使用
'''
# 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
print(chardet.detect(b'Hello, world!'))
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

'''
psutil
用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，
还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
'''
# CPU逻辑数量
print(psutil.cpu_count())

# CPU物理核心
print(psutil.cpu_count(logical=False))

# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

#实现类似top命令的做法
for x in range(10):
    psutil.cpu_percent(interval=1, percpu=True)

#使用psutil获取物理内存和交换内存信息，分别使用：
print(psutil.virtual_memory())
print(psutil.swap_memory())


#获取磁盘信息
# 磁盘分区信息
print(psutil.disk_partitions())
# 磁盘使用情况
print(psutil.disk_usage('/'))
# 磁盘IO
print( psutil.disk_io_counters())

#获取网络信息 等等,省略获取进程信息示例代码
print(psutil.net_if_addrs())