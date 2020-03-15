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


    values_anal = analitick(l, D, c, alpha, T, I)
    charts(values, x, values_anal)

    # расчёт погрешности
    epsilon = abs(values - values_anal)
    k = 0
    for i in range(len(epsilon)):
        max_epsilon = max(epsilon)
        k = i
    print(max_epsilon, " ", i)



def charts(values_y_alg, values_x, values_y_anal ):
    plt.title("Динамическое поле концентрации в трубке")
    plt.xlabel("длина трубки, l")
    plt.ylabel("u(x,t)")
    plt.plot(values_x, values_y_alg, color = 'red', label = "Численное решение")
    plt.plot(values_x, values_y_anal, color = 'blue', label = "Аналитическое решение")
    plt.grid()
    plt.legend()
    plt.show()



def analitick(l, D, C, alpha, T, I):
    k = 1
    h_x = l / I
    x = np.arange(0, l + h_x, h_x)
    X_k = np.cos(np.pi * x * k / l)
    temp = T * ((alpha / C) * (np.pi * k / l) ** 2 + D / C)
    T_k = np.exp(-temp)
    A_k = (l/2)
    u =  X_k * T_k *A_k
    return u

if __name__ == "__main__":
    l, D, c, alpha, T, I, K = 4, 0.002, 1.5, 0.08,  10, 64, 512
    alg(l, D, c, alpha, T, I, K )

    #T = 10, измельчать сетку пока они почти не совпадут







