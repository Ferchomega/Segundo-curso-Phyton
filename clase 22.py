student_uid = [1,2,3]
students = ["Juan", "Jose", "Larsen"]
students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print(students_with_uid)


import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,3))
non_repeated = {number for number in random_numbers}
print(random_numbers)
print(non_repeated)