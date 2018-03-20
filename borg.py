# -*- coding: utf-8 -*-

"""
共享模式
由单例模式衍生出来，因为python的特性在class实例化的时候，每次调用都是使用这个对象的缓存，由此实现了资源的共享。
所有实例都共享同一个__dict__.



参考资料
https://fkromer.github.io/python-pattern-references/design/#singleton

"""

class Born(object):

    __share_state = {}

    def __init__(self):
        self.__dict__ = self.__share_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class SelfBorn(Born):
    pass

if __name__ == '__main__':
    rm1 = Born()
    rm2 = Born()
    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = SelfBorn()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))


### OUTPUT ###
# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 140732837899224
# rm2 id: 140732837899296
# rm1: Init
# rm2: Init
# rm3: Init