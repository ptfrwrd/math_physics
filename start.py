import numpy as np
import matplotlib.pyplot as plt


# трехдиагональная матрица
def create_matrix(gamma, coeff_B, I):
    matrix = np.zeros((I, I))
    flat = matrix.ravel()
    flat[0::I + 1] = coeff_B
    flat[I::I + 1] = -gamma
    flat[1::I + 1] = -gamma
    flat[1], flat[-2] = -2 * gamma, -2 * gamma
    return matrix


# Вычисление гаммы для неявной схемы
def get_gamma(h_t, h_x, alpha, c):
    return h_t * alpha / ((h_x ** 2) * c)


# Прогонка для неявной схемы
def alg(l, D, c, alpha, T, I, K):
    h_x, h_t = l / I, T / K
    x = np.arange(0, l + h_x, h_x)
    t = np.arange(0, T + h_t, h_t)
    gamma = get_gamma(h_t, h_x, alpha, c)
    coeff_B = 1 + 2 * gamma + h_t * D / c
    values_numerical = np.cos(np.pi * x / l)
    matrix_P = create_matrix(gamma, coeff_B, I + 1)
    for k in range(len(t)):
        values_numerical = np.linalg.solve(matrix_P, values_numerical)


    values_anal = analytically(l, D, c, alpha, T, I)
    charts(values_numerical, x, values_anal)

    # расчёт погрешности
    epsilon = abs(values_numerical - values_anal)
    k = 0
    for i in range(len(epsilon)):
        max_epsilon = max(epsilon)
        k = i
    print(max_epsilon, " ", i)


# построение графиков
def charts(values_y_alg, values_x, values_y_anal ):
    plt.title("Динамическое поле концентрации в трубке")
    plt.xlabel("длина трубки, l")
    plt.ylabel("u(x,t)")
    plt.plot(values_x, values_y_alg, color = 'red', label = "Численное решение")
    plt.plot(values_x, values_y_anal, color = 'blue', label = "Аналитическое решение")
    plt.grid()
    plt.legend()
    plt.show()


# аналитическое решение
def analytically(l, D, C, alpha, T, I):
    k = 1
    h_x = l / I
    x = np.arange(0, l + h_x, h_x)
    X_k = np.cos(np.pi * x * k / l)
    temp = T * ((alpha / C) * (np.pi * k / l) ** 2 + D / C)
    T_k = np.exp(-temp)
    A_k = 1
    u =  X_k * T_k *A_k
    return u

