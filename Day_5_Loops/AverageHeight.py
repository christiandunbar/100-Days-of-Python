student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

students_count = 0
total_height = 0

for n in student_heights:
    students_count += 1
    total_height += n

average = total_height / students_count
print(average)
