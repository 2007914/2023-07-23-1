import random

def score(students_num:int) ->list:
    students = []
    for i in range(students_num):
        one_student = [random.randint(50,100) for _ in range(5)]
        students.append( one_student)
    return students