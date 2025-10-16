import csv

emp = []
n= int(input("Enter the number of employees "))
for i in range(n):
    details = input("Enter the details of student seprated by comma(Name, dept, Salary):")
    (name, dept, salary) = details.split(',')
    emp.append([name, dept, int(salary)])

with open('employee.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Dept", "Salary"])
    writer.writerows(emp)

print("\n Details updated successfully")


with open('employee.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    salaries = []
    heighest = ("", 0)


    print("\n Reading data from filee...\n")
    print("Employee details:")

    for row in reader:
        name = row['Name']
        dept = row['Dept']
        salary = int(row['Salary'])

        print(f"{name} | {dept} | {salary}")

        salaries.append(salary)
        if salary > heighest[1]:
            heighest = (name,salary)

print(f"\n HIGHEST SALARY: {heighest[0]}({heighest[1]})")
print(f"\n AVERAGE SALARY: {sum(salaries)/len(salaries)}")


