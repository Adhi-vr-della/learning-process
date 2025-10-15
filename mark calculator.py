# base details

name = input("Enter your name: ")
s = int(input("Enter the number subjects: "))

# initialize the list for subjects

subject = []


#  loop for get a sub's mark
for i in range(s):
    sub= float(input(f"The mark of the {i+1} subject :"))
    subject.append(sub)


#  for total
total = sum(subject)


# for average
avg = total / len(subject)

# output


print("Name of the student is:", name)
print("The total no of subjects:", s)
print("The Total mark is:", total)
print("The average of the mark is :", avg)



# for grading system

if avg >=90:
    print("You got a 'A' grade!")
elif avg >=80 and avg <=89:
    print("You got a 'B' grade!")
elif avg >=70 and avg <=79:
    print("You got a 'C' grade!")
elif avg >=60 and avg <=69:
    print("You got a 'D' grade!")
elif avg<=60 and avg>=35 :
    print("You got a 'F' grade!")
else:
    print("you are fail, study well, better luck next time!")