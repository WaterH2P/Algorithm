
import json

d = dict(name='H2P', age=21, score=100)
j = json.dumps(d)
print(j)

s = '{"name": "H2P", "age": 21, "score": 100}'
j2 = json.loads(s)
print(j2)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def Std2Dict(std):
    return {
        'name'  : std.name,
        'age'   : std.age,
        'score' : std.score
    }

s = Student('H2P', 21, 100)
print(json.dumps(s, default=Std2Dict))