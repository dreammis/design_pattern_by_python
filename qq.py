from __future__ import print_function

__metaclass__ = type


class Bird:
    def __init__(self):
        print('���Ǹ���ĳ�ʼ��')
        self.cansing = True

    def eat(self):
        print('i can eat')

    def sing(self):
        if self.cansing:
            print('i can sing')


class Sparrow(Bird):
    def __init__(self):
        super(Sparrow, self).__init__()
        print('�Ҿ���Ҫ��д�����init')

    def jump(self):
        print('i can jump')


S = Sparrow()
S.jump()
S.eat()
S.sing()
