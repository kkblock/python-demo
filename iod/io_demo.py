# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO
import os

#读文件
#如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
f = open('/home/black/Documents/vim-help.txt', 'r')
print(f.read())
#最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
f.close()

#增加异常处理部分
try:
    f = open('/home/black/Documents/vim-help.txt', 'r')
finally:
    if f:
        f.close()

#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('/home/black/Documents/vim-help.txt', 'r') as f:
    print(f.read())
    # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

#字符编码
f = open('/home/black/Documents/vim-help.txt', 'r',encoding='UTF-8')
f.read()
f.close()

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，
# 表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('/home/black/Documents/vim-help.txt', 'r',encoding='UTF-8',errors='ignore')
f.read()
f.close()


#写文件
#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('/home/black/Documents/vim-help2.txt', 'w',encoding='UTF-8')
f.write('hello world')
f.close()

#StringIO和BytesIO
#很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO顾名思义就是在内存中读写str。

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#BytesIO StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。 BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#操作文件和目录
'''
如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
'''
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)

#环境变量
print(os.environ)
print(os.environ.get('HOME'))

#操作文件和目录
'''
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
'''
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/home', 'black'))
# 创建 os.mkdir() 删除rmdir()
#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

#幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

#序列化
'''
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。
'''
# 序列化  pickle.dump(d, f)
# d = pickle.load(f)

#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：json.dumps(d)

#print(json.dumps(s, default=lambda obj: obj.__dict__))

