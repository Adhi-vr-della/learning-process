# to get input
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height(cm): "))
stu = str(input("Are you a student?(Yes/No): "))


#data process

data_hig = height/100
is_stu = stu.lower() == "yes"

# output

print("your name is", name)
print("your age is", age)
print("your height is", round(data_hig, 2),"meters")
print("Student status is", is_stu)
