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

    def get_name(self):
        return f"{self.surname} {self.name[0]}. {self.patronymic[0]}."

    def get_classroom(self):
        return f"{self.class_room}"


class Parent(Person):
    def __init__(self, surname, name, patronymic, gender):
        super().__init__(surname, name, patronymic, gender)
        self.childs = []

    def set_childs(self, child):
        self.childs.append(child)


class Teacher(Person):
    def __init__(self, surname, name, patronymic, subject):
        super().__init__(surname, name, patronymic)
        self.subject = subject

    def get_subject(self):
        return f"{self.subject}"


class Classroom:
    def __init__(self, class_room, subject1, subject2, subject3, subject4):
        self.class_room = class_room
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.subject4 = subject4

    def get_subjects(self):
        return f"{self.subject1}, {self.subject2}, {self.subject3}, {self.subject4}"

    def get_classroom(self):
        return f"{self.class_room}"




subjects = ["Математика", "Русский", "Литература", "Физика", "Труд", "Рисование", "Природоведение", "Язык",
            "Физкультура"]

classrooms = [Classroom("2 А", subjects[0], subjects[1], subjects[2], subjects[3]),
              Classroom("3 А", subjects[2], subjects[3], subjects[4], subjects[5]),
              Classroom("2 Б", subjects[4], subjects[5], subjects[6], subjects[7]),
              Classroom("3 Б", subjects[5], subjects[6], subjects[7], subjects[8])]

fathers = [Parent("Сидоров", "Павел", "Павлович", "М"),
           Parent("Гаскин", "Павел", "Семенович", "М"),
           Parent("Светлов", "Николай", "Николаевич", "М"),
           Parent("Юров", "Семен", "Прокофьевич", "М"),
           Parent("Краснов", "Лаврентий", "Михайлович", "М"),
           Parent("Александров", "Николай", "Петрович", "М"),
           Parent("Петров", "Павел", "Николаевич", "М"),
           Parent("Левченко", "Семен", "Павлович", "М"),
           Parent("Сысоев", "Николай", "Геннадьевич", "М"),
           Parent("Калашников", "Дмитрий", "Николаевич", "М"),
           Parent("Немов", "Семен", "Павлович", "М"),
           Parent("Слепцов", "Павел", "Лаврентьевич", "М")]

mothers = [Parent("Сидорова", "Наталья", "Михайловна", "Ж"),
           Parent("Гаскина", "Светлана", "Игоревна", "Ж"),
           Parent("Светлова", "Мария", "Александровна", "Ж"),
           Parent("Юрова", "Евгения", "Витальевна", "Ж"),
           Parent("Краснова", "Ксения", "Павловна", "Ж"),
           Parent("Александрова", "Наталья", "Вячеслововна", "Ж"),
           Parent("Петрова", "Наталья", "Александровна", "Ж"),
           Parent("Левченко", "Наталья", "Юрьевна", "Ж"),
           Parent("Сысоева", "Мария", "Николаевна", "Ж"),
           Parent("Калашникова", "Наталья", "Вячеславовна", "Ж"),
           Parent("Немова", "Александра", "Михайловна", "Ж"),
           Parent("Слепцова", "Наталья", "Геннадьевна", "Ж")]

students = [Student("Сидоров", "Степан", "Павлович", fathers[0], mothers[0], classrooms[0].get_classroom()),
            Student("Гаскина", "Мария", "Павловна", fathers[1], mothers[1], classrooms[0].get_classroom()),
            Student("Светлова", "Нина", "Николаевна", fathers[2], mothers[2], classrooms[0].get_classroom()),
            Student("Юров", "Николай", "Семенович", fathers[3], mothers[3], classrooms[1].get_classroom()),
            Student("Краснова", "Мария", "Лаврентьевна", fathers[4], mothers[4], classrooms[1].get_classroom()),
            Student("Александров", "Степан", "Николаевич", fathers[5], mothers[5], classrooms[1].get_classroom()),
            Student("Петрова", "Елизавета", "Павловна", fathers[6], mothers[6], classrooms[2].get_classroom()),
            Student("Левченко", "Маргарита", "Семеновна", fathers[7], mothers[7], classrooms[2].get_classroom()),
            Student("Сысоев", "Степан", "Николаевич", fathers[8], mothers[8], classrooms[2].get_classroom()),
            Student("Калашникова", "Надежда", "Дмитриевна", fathers[9], mothers[9], classrooms[3].get_classroom()),
            Student("Немова", "Мария", "Семеновна", fathers[10], mothers[10], classrooms[3].get_classroom()),
            Student("Слепцова", "Зинаида", "Павловна", fathers[11], mothers[11], classrooms[3].get_classroom())]

teachers = [Teacher("Иванова", "Мария", "Ивановна", subjects[0]),
            Teacher("Петрова", "Нина", "Степановна", subjects[1]),
            Teacher("Сидорова", "Екатерина", "Матвеевна", subjects[2]),
            Teacher("Лопухина", "Мария", "Петровна", subjects[3]),
            Teacher("Иванова", "Лидия", "Сергеевна", subjects[4]),
            Teacher("Кошелева", "Нина", "Семеновна", subjects[5]),
            Teacher("Ивлева", "Надежда", "Петровна", subjects[6]),
            Teacher("Иванова", "Клавдия", "Ивановна", subjects[7]),
            Teacher("Науменко", "Мария", "Станиславовна", subjects[8])]



def listclass():
    for classroom in classrooms:
        print(classroom.get_classroom())


def get_students_in_class(classroom):
    for student in students:
        if student.get_classroom() == classroom.get_classroom():
            print(student.get_name())

def get_subject_in_student(student):
    for classx in classrooms:
        if student.get_classroom() == classx.get_classroom():
            print(classx.get_subjects())

def get_parents(student):
    print(student.get_parents_name())

def get_teachers(classroom):
    for teacher in teachers:
        if teacher.subject in classroom.get_subjects():
            print(teacher.full_name())


listclass()
get_students_in_class(classrooms[1])
get_subject_in_student(students[1])
get_parents(students[1])
get_teachers(classrooms[0])

