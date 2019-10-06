from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
day2 = Weekday.Tue
print(day1)
print(day2)
print(Weekday.Mon.value)

for name, mem in Weekday.__members__.items():
    print(name, '=>', mem)