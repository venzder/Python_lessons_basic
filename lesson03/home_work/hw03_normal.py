# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonacci(n, m):
#     fib = []
#     for i in range(n, m)
#
#
# print(fibonacci(1, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#     n = 1
#     while n < len(origin_list):
#         for i in range(len(origin_list) - n):
#             if origin_list[i] > origin_list[i + 1]:
#                 origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
#         n += 1
#     return origin_list
#
#
# print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

x = [4, 5, 7, 9]
def func(x):
    if x % 3 == 0:
        return 1
    else:
        return 0

def filter_list(fn, list_1):
    list_2 = []
    for i in list_1:
        if fn(i) == True:
            list_2.append(i)
    return list_2

print(filter_list(func, x))



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
