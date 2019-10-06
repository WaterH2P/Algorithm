
# 多重继承
class Animal(object):
    pass


class Mammal(Animal):
    pass

class Bird(Animal):
    pass


class RunableMixln(object):
    def run(self):
        print('Run...')

class FlyableMixln(object):
    def fly(self):
        print('Fly...')


class Dog(Mammal, RunableMixln):
    pass

class Bat(Mammal, FlyableMixln):
    pass