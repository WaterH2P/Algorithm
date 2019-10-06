def person(name, age, *args, city, job):
    print(name)
    print(age)
    for arg in args:
        print(arg)
    print(city)
    print(age)

person('Mike', 20, 'sb', 'nb', city='Beijing', job='Engineer')