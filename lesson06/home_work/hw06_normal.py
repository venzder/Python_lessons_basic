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
    def __init__(self, surname, name, patronymic, gender=None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.gender = gender

    def full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class Student(Person):
    def __init__(self, surname, name, patronymic, father, mother, class_room):
        super().__init__(surname, name, patronymic)
        self.class_room = class_room
        self.father = father
        self.mother = mother
        self.assign_to_parents()

    def get_parents_name(self):
        return f'{self.father.full_name()}, {self.mother.full_name()}'

    def assign_to_parents(self):
        self.father.set_childs(self)
        self.mother.set_childs(self)


class Parent(Person):
    def __init__(self, surname, name, patronymic, gender):
        super().__init__(surname, name, patronymic, gender)
        self.childs = []

    def set_childs(self, child):
        self.childs.append(child)


class Teacher(Person):
    def __init__(self, surname, name, patronymic, subject):
        super().__init__(self, surname, name, patronymic)
        self.subject = subject

    def get_subject(self):
        return self.subject


class Classroom:
    def __init__(self, class_room, subject1, subject2, subject3, subject4):
        self.class_room = class_room
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.subject4 = subject4

    def get_subjects(self):
        return f"{self.subject1}, {self.subject2}, {self.subject3}, {self.subject4}"




subjects = ["Математика", "Русский", "Литература", "Физика", "Труд", "Рисование", "Природоведение", "Язык",
            "Физкультура"]
teachers = [Teacher("Иванова", "Мария", "Ивановна", subjects[0]),
            Teacher("Петрова", "Нина", "Степановна", subjects[1]),
            Teacher("Сидорова", "Екатерина", "Матвеевна", subjects[2]),
            Teacher("Лопухина", "Мария", "Петровна", subjects[3]),
            Teacher("Иванова", "Лидия", "Сергеевна", subjects[4]),
            Teacher("Кошелева", "Нина", "Семеновна", subjects[5]),
            Teacher("Ивлева", "Надежда", "Петровна", subjects[6]),
            Teacher("Иванова", "Клавдия", "Ивановна", subjects[7]),
            Teacher("Науменко", "Мария", "Станиславовна", subjects[8])]

classrooms = [Classroom("2 А", subjects[0], subjects[1], subjects[2], subjects[3]),
              Classroom("3 А", subjects[2], subjects[3], subjects[4], subjects[5]),
              Classroom("2 Б", subjects[4], subjects[5], subjects[6], subjects[7]),
              Classroom("3 Б", subjects[5], subjects[6], subjects[7], subjects[8])]


def get_teachers(classroom):
    techers_class = [teacher.full_name() for teacher in teachers if teacher.subject in classroom.get_subjects()]
    return techers_class


print(teachers[1].full_name())
print(classrooms[1].get_subjects())
print(get_teachers(classrooms[0]))