# def factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)


# def factorial_iterative(n):
#     """
#     Computes the factorial of a non-negative number n (using iteration)
#     """
#     if n == 0:
#         return 1
#
#     current_result = 1
#
#     for i in range(n):
#         current_result += i * current_result
#
#     return current_result
#
#
# result = factorial_iterative(5)
# print(result)

#
# def nat():
#     n = 0
#     while True:
#         n += 1
#         yield n
#
#
# gen = nat()
# for _ in range(5):
#     print(next(gen))


# def nat():
#     """Returns all natural numbers"""
#     n = 0
#     while True:
#         n += 2
#         yield n
#
# gen = nat()
# for _ in range(10):
#     print(next(gen))


# def factorial_gen():
#     n = 1
#     result = 1
#     while True:
#         result *= n
#         yield result
#         n += 1
#
#
# gen = factorial_gen()
# for _ in range(5):
#     print(next(gen))


# def fibonacci(n):
#     fibo = []
#
#     for x in range(n):
#         if len(fibo) < 2:
#             fibo.append(1)
#         else:
#             fibo.append(fibo[-1] + fibo[-2])
#
#     return fibo
#
#
# res = fibonacci(10)
# print(res)


import numpy as np
import matplotlib.pyplot as plt

# Размер на изображението
width, height = 800, 800

# Създаваме координатна мрежа
x = np.linspace(-2, 1, width)
y = np.linspace(-1.5, 1.5, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.zeros_like(C)
iterations = np.zeros(C.shape, dtype=int)

# Максимален брой итерации
max_iter = 100

# Основен цикъл за изчисление на фрактала
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask] ** 2 + C[mask]
    iterations[mask] = i

# Визуализиране
plt.figure(figsize=(8, 8))
plt.imshow(iterations, cmap='inferno', extent=(-2, 1, -1.5, 1.5))
plt.axis('off')
plt.title('Манделброт фрактал', fontsize=16)
plt.show()














































