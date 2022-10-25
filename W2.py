# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def prod_lst(list):
    l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
    print(new_list)
list = [2, 3, 4, 5, 6]
prod_lst(list)