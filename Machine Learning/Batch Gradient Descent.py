# 梯度下降
import numpy as np

# 根据代价函数逐个更新 K
def BatchGradientDescentRespectively(xs, ys, a) -> list:
    xs = [[1, *x] for x in xs]
    m, n = len(xs), len(xs[0])
    K, PDs = [0] * n, [float('inf')] * n
    while max(map(abs, PDs)) > 0.000001:
        Error = [sum([K[j] * xs[i][j] for j in range(n)]) - ys[i] for i in range(m)]
        PDs = [sum([Error[i] * xs[i][j] for i in range(m)]) * a / m for j in range(n)]
        K = [K[i] - PDs[i] for i in range(n)]
    return K


# 矩阵计算梯度下降
def BatchGradientDescentByVector(xs, ys, a) -> list:
    m = len(xs)
    vXs = np.mat([[1.0, *x] for x in xs])
    vYs = np.mat([[y] for y in ys])
    vKs = np.mat([[0.0] for _ in range(len(xs[0]) + 1)])
    vPD = a * vXs.T * (vXs * vKs - vYs) / m
    while max(map(abs, vPD)) > 0.000001:
        vKs -= vPD
        vPD = a * vXs.T * (vXs * vKs - vYs) / m
    return vKs.T.tolist()[0]


if __name__ == "__main__":
    a = 0.005
    xs = [[1], [2], [3], [4], [5], [6]]
    ys = [2, 4, 6, 8, 10, 12]
    print(BatchGradientDescentRespectively(xs, ys, a))
    print(BatchGradientDescentByVector(xs, ys, a))