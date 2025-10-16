'''You’re building a simple program to calculate and analyze employee salaries.
You’ll use functions in different ways to complete it.'''


employee =list(map(str,input("Enter the employee details(Name,Base salary, dept) ").split()))

emp= []
for i in employee:
    rec = i.split(",")
    name=rec[0]
    base=int(rec[1])
    dept=rec[2]
    emp.append((name,base,dept))


print("Employee Details:")
print(emp)
em={}
def cal_bounce(emp,rate=0.1):
    for name,base,dept  in emp:
        bonus = base * rate
        if name not in em:
            em[name] = bonus
        em[name] = bonus

    return em


def update_salary(name,salary,bonus):
        new_salary = salary + bonus
        return new_salary

bounce_dict = cal_bounce(emp,rate=0.1)

print("Bounce Info",bounce_dict)

print("Employee Details:")
print(emp)

print("Bounce Info",bounce_dict)

for name,base,dept in emp:
    bounce = bounce_dict[name]
    salary = update_salary(name,base,bounce)
    print(f"{name} ({dept}) → Base Salary: {base}, Bonus: {em[name]}, New Salary: {salary}")


