# -*- coding: utf-8 -*-

if 1 < 2:
    print('aaa')

# 接收输入
# birth = input('birth: ')
# birth = int(birth)
#
# if birth > 2:
#     print('a')
# elif birth < 2:
#     print('b')
# else:
#     print('c')


names = ['Michael', 'Bob', 'Tracy']
for n in names:
    print(n)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += x
print(sum)

#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print(list(range(10)))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#第二种循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#break continue 和java中使用的方式是一样的