# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))
def fibonacci(n):
    numb = []
    a, b = 1, 1
    for i in range(n):
        numb.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        numb.insert(0, a)
        a, b = b, a - b
    return numb

numb = fibonacci(n)
print(fibonacci(n))