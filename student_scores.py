student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

score = 0

for high in student_scores:
    if high > score:
        score = high

print(score)
