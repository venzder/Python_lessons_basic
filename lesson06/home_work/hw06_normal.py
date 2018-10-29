# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def full_name(self):
        return f"{self.name} {self.surname} {self.patronymic}"


class Student(Person):
    def __init__(self, name, surname, patronymic, class_room):
        super(Student, self).__init__(name, surname, patronymic)
        self.class_room = class_room


class Teacher(Person):
    def __init__(self, name, surname, patronymic, subject):
        super(Teacher, self).__init__(name, surname, patronymic)
        self.subject = subject


class Mother(Person):
    def __init__(self, name, surname, patronymic):
        super(Mother, self).__init__(name, surname, patronymic)


class Dad(Person):
    def __init__(self, name, surname, patronymic):
        super(Dad, self).__init__(name, surname, patronymic)


class Classroom:
    def __init__(self, class_num, subject1):
