class Student(object):

    def __init__(self, val):
        self._birth = val

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, val):
        self._birth = val

    @property
    def age(self):
        return 2019 - self._birth

std = Student(1998)
print(std.age)
std.birth = 2000
print(std.age)