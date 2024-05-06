student_heights = [180, 124, 165, 173, 189, 169, 146]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

somme = 0
nr_student = 0
for height in student_heights:
    somme += height
for student in student_heights:
    nr_student += 1

average = somme/nr_student
print(f"The average height is {round(average)}.")
