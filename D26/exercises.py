import random

numbers = [1, 2, 3]
new_list = [numb + 1 for numb in numbers]

print(new_list)


name = "Tsibo"
new_list_name = [letter for letter in name]

print(new_list_name)


names = ["Alex", "Big Joe The Legende", "Dave", "Caroline"]

long_names = [name.upper() for name in names if len(name) > 5]

print(long_names)

student_scores = {student: random.randint(1, 100) for student in names}

passed_students = {
    student: grade for (student, grade) in student_scores.items() if grade >= 60
}

print(passed_students)
