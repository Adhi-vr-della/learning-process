from grade_assign import calculate_avg,assign_grade
import sat


student = {}

n= int(input("Enter the number of students: "))
for i in range(n):
    name = input(f" \nEnter student{i+1} name: ")
    mark = input("Enter the mark of student seprated by comma:")
    mark = [int(x) for x in mark.split(',')]
    student[name] = mark



print("Student Details:")
print(student)

for name, marks in student.items():
    avg = calculate_avg(marks)
    grade = assign_grade(avg)
    print(f"{name}: Average = {avg:.2f}, Grade = {grade}")
print("\nClass average:", sat.find_class_average(student))
print("Top student:", sat.find_highest_mark(student))




