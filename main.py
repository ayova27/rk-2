def task2():
    import random
    discipline = {
        "math": 4,
        'Chemistry': 3,
        'English': 4
    }

    score = {
        "Math": 85,
        'Chemistry': 73,
        'English': 91
    }

    gpas = {
        95: 4.3,
        90: 4.0,
        85: 3.7,
        80: 3.3,
        75: 3.0,
        70: 2.7,
        65: 2.3,
        60: 2.0,
        55: 1.7,
        50: 1.3,
        45: 1.0,
        40: 0.7
    }

    lists_math = []
    lists_english = []
    lists_chemistry = []

    with open('credits.txt', 'w') as credit:
        for name_discipline, creditss in discipline.items():
            creditss = str(creditss)
            credit.write(name_discipline + ' ')
            credit.write(creditss + '\n')

    with open('math.txt', 'w') as math:
        for score in range(15):
            random_int_math = str(random.randint(55, 100))
            lists_math.append(int(random_int_math))
            math.write(random_int_math + '\n')

    with open('english.txt', 'w') as math:
        for score in range(15):
            random_int_english = str(random.randint(55, 100))
            lists_english.append(int(random_int_english))
            math.write(random_int_english + '\n')

    with open('chemistry.txt', 'w') as math:
        for score in range(15):
            random_int_chemistry = str(random.randint(55, 100))
            lists_chemistry.append(int(random_int_chemistry))
            math.write(random_int_chemistry + '\n')


task2()


def task3():
    class Student:
        def __init__(self, name, number_courses, scores, gpa):
            self.name = name
            self.number_courses = number_courses
            self.scores = scores
            self.gpa = gpa

        def setStatus(self):
            if self.gpa > 1:
                return 'learning'

        def showGPA(self):
            return self.gpa

        def gpa(self):
            gpa = self.gpa


    student1 = Student('Daulet', 3, {'math': {'score': 4.3, 'credits': 4}, 'chemistry': {'score': 3.3, 'credits': 3},
                                     'english': {'score': 4.0, 'credits': 4}}, 3.75)
    student2 = Student('Akzhol', 3, {'math': {'score': 4.2, 'credits': 4}, 'chemistry': {'score': 3.1, 'credits': 3},
                                     'english': {'score': 4.5, 'credits': 4}}, 3.2)

    students = [student1, student2]
    gpa_input = []
    n = 0
    for x in students:
        gpa_input.append(Student.gpa(x))





