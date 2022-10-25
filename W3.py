# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def float_min_max(list):
    minf = 1.
    maxf = 0.
    for i in range(len(list)):
        curr = round(list[i] - int(list[i]), 2)
        if curr != 0.:
            if curr < minf:
                 minf = curr
            if curr > maxf:
                maxf = curr
    return maxf - minf
list = [1.1, 1.2, 3.1, 5, 10.01]
print(float_min_max(list))