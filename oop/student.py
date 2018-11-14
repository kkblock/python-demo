# -*- coding: utf-8 -*-

class Student(object):

    sex = '男'#这是类属性,类的所有实例都可以访问到


    # def __init__(self,name,score):
    #     self.name = name
    #     self.score = score

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def hello(self):
        print(self.__name,self.__score)

    def print_score(std):
        print('%s: %s' % (std.__name, std.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    #增加set方法
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_name(self,name):
        self.__name = name