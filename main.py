#by K9

import numpy as np
import time
import matplotlib.pyplot as plt


# 1. Посчитать время выполнения арифметической операции
def time_arithmetic_operation():
    start_time = time.time()
    result = 123456789 * 987654321  # Пример арифметической операции
    end_time = time.time()
    print(f"Время выполнения арифметической операции: {end_time - start_time:.10f} секунд")
    return result


# 2. Посчитать время генерации массива из N чисел
def time_array_generation(N):
    start_time = time.time()
    array = [i for i in range(N)]  # Генерация массива
    end_time = time.time()#by K9
    print(f"Время генерации массива из {N} чисел: {end_time - start_time:.10f} секунд")
    return array


# 3. Генерация матрицы и сравнение с Numpy
def generate_matrix_custom(N, M, low, high):
    return [[np.random.randint(low, high) for _ in range(M)] for _ in range(N)]


def compare_matrix_generation(N, M, low, high):
    # Время генерации матрицы с помощью пользовательской функции
    start_time_custom = time.time()
    custom_matrix = generate_matrix_custom(N, M, low, high)
    end_time_custom = time.time()#by K9

    # Время генерации матрицы с помощью Numpy
    start_time_numpy = time.time()
    numpy_matrix = np.random.randint(low, high, size=(N, M))
    end_time_numpy = time.time()

    print(
        f"Время генерации матрицы {N}x{M} (пользовательская функция): {end_time_custom - start_time_custom:.10f} секунд")
    print(f"Время генерации матрицы {N}x{M} (Numpy): {end_time_numpy - start_time_numpy:.10f} секунд")


# 4. Итеративная функция расчета факториала и построение графика
def factorial(n):
    result = 1#by K9
    for i in range(2, n + 1):
        result *= i
    return result


def plot_factorial_times():
    inputs = [10, 30, 50, 100, 200, 300, 500, 1000]
    times = []

    for n in inputs:
        start_time = time.time()
        factorial(n)
        end_time = time.time()#by K9
        times.append(end_time - start_time)

    plt.plot(inputs, times, marker='o')
    plt.title("Время выполнения расчета факториала")
    plt.xlabel("n")
    plt.ylabel("Время (секунды)")
    plt.grid()
    plt.show()


# Выполнение всех задач
if __name__ == "__main__":
    time_arithmetic_operation()
    time_array_generation(100000)
    compare_matrix_generation(1000, 1000, 0, 10)
    plot_factorial_times()
    print(f"\nby K9")