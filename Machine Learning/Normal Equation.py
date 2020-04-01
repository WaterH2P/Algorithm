# 正规方程
import numpy as np

# K = (X^T * X)^{-1} * X^T * Y
def NormalEquation(xs, ys, a) -> list:
    mXs = np.mat([[1.0, *x] for x in xs])
    mYs = np.mat([[y] for y in ys])
    vKs = (mXs.T * mXs).I * mXs.T * mYs
    return vKs.T.tolist()[0]


if __name__ == "__main__":
    a = 0.005
    xs = [[1], [2], [3], [4], [5], [6]]
    ys = [2, 4, 6, 8, 10, 12]
    print(NormalEquation(xs, ys, a))