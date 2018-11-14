# -*- coding: utf-8 -*-

class Student(object):

    sex = '男'#这是类属性,类的所有实例都可以访问到

    __slots__ = ('__name', '__score')  # 用tuple定义允许绑定的属性名称

    # def __init__(self,name,score):
    #     self.name = name
    #     self.score = score

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    #不用设置这个方法因为@property标记的方法已经是返回get,若定义只读方法,可以只设置getter
    @score.getter
    def score(self):
        return self.__score

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