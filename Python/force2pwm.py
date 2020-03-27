def force2pwm(val):
    return (val - 8.232) / (27.44 - 8.232) * 1000 + 1000

def force2pwm2(val):
    return (val - 0) / (19.6 - 0) * 1000 + 1000

def pwm2force(val):
    return (val - 1000) / (2000 - 1000) * (27.44 - 8.232) + 8.232

def pwm2force2(val):
    return (val - 1000) / (2000 - 1000) * (19.6 - 0)

if __name__ == '__main__':
    force = 22.09
    print(force2pwm(force))

    force2 = 6.45
    print(force2pwm2(force2))

    pwm = 1660
    print(pwm2force(pwm))

    pwm2 = 1450
    print(pwm2force2(pwm2))