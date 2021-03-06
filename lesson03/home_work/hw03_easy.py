# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def my_round(number, ndigits):
#     r_number = list(f"{number:.{ndigits + 1}f}")
#     if int(r_number[-1]) < 5:
#         r_number[-2] = int(r_number[-2])
#         r_number = r_number[:-1]
#         r_number = float("".join(str(x) for x in r_number))
#         return r_number
#     else:
#         r_number[-2] = int(r_number[-2]) + 1
#         r_number = r_number[:-1]
#         r_number = float("".join(str(x) for x in r_number))
#         return r_number
#
#
#
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    block_1 = list(map(int, list(str(ticket_number // 1000))))
    block_2 = list(map(int, list(str(ticket_number % 1000))))
    if sum(block_1) == sum(block_2):
        return "Счастливый билет"
    else:
        return "Несчастливый билет"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
