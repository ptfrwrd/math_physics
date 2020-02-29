import numpy as np
import matplotlib.pyplot as plt


# Вычисление гаммы для неявной схемы
def get_gamma(h_t, h_x, alpha, c):
    return h_t * alpha / ((h_x ** 2) * c)


# Прогонка для неявной схемы
def alg(l, D, c, alpha, T, I, K):
    # поиск h_x, h_t
    h_x, h_t = l/I, T/K
    # заполняем массив [0, l + h_x]
    x = np.arange(0, l + h_x, h_x)
    # заполняем массив [0, T + h_t]
    t = np.arange(0, T + h_t, h_t)
    # на слое k = 0 значения u_i:
    values = np.cos(np.pi * x / l)
    # рассчитываем значение gamma
    gamma = get_gamma(h_t, h_x, alpha, c)
    # т.к. диагональ матрицы состоит из одного элемента, то все кладем в переменную
    coefficient_B = 1 + 2 * gamma + h_t * D / c
    # заведём массив для хранения прогоночных коэффициентов: b_i (на каждом k-ом слое разное) и a_i
    coefficients_a, coefficients_b = [], []
    for k in np.arange(0, len(t) - 1, 1):
        for i in np.arange(0, len(x), 1):
            if i == 0:
                coefficients_a.append(2 * gamma / coefficient_B)
                coefficients_b.append(values[i]/coefficient_B)
                values[i] = coefficients_a[i] * values[i] + coefficients_b[i]
            else:
                coefficient_A, coefficient_C = -gamma, -gamma
                coefficient_F = values[i]
                coefficients_a.append(- coefficient_A / (coefficient_B +
                                                          coefficient_C * coefficients_a[i-1]))
                coefficients_b.append((coefficient_F - coefficient_C * coefficients_b[i-1])
                                       / (coefficient_B + coefficient_C * coefficients_a[i-1]))
                values[i] = coefficients_a[i] * values[i] + coefficients_b[i]

        # надо впихнуть обратную прогонку
        for i in np.arange(len(x) - 2, -1, -1):
            values[i] = coefficients_a[i] * values[i + 1] + coefficients_b[i]

    charts(values, x)
    return values


def charts(values_y, values_x ):
    plt.title("Динамическое поле концентрации в трубке")
    plt.xlabel("длина стержня, l")
    plt.ylabel("u(x,t)")
    plt.grid()
    plt.legend("Неявная схема")
    plt.plot(values_x, values_y, color = 'red')
    plt.show()

if __name__ == "__main__":
    print(alg(2, 0.02, 0.8, 0.24,  10, 25, 200))







