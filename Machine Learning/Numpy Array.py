import numpy

if __name__ == "__main__":
    a = numpy.array([
        [2, 2],
        [2, 2]
        ])
    b = numpy.array([1, 2])

    print(numpy.dot(a, b))