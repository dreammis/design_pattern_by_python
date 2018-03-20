# -*- coding: utf-8 -*-

"""
工厂模式旨在提供一个接口(interface)，供那些相关的对象去使用，不需要特别指定他们的类(class)

参考资料
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

"""

import random


class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog(object):

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


def random_animal():
    return random.choice([Dog, Cat])()


if __name__ == '__main__':
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()

    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()


### OUTPUT ###
# We have a lovely Cat
# It says meow
#
# We have a lovely Dog
# It says woof
# ====================
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Cat
# It says meow
# ====================