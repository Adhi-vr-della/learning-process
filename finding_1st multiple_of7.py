s = list(map(int, input("Enter the student's marks: ").split()))

flag = False

for x in s:
    if(x%7==0):
        print("First Multiple of 7 in a List:", x)
        flag = True
        break
if not flag:
    print("There is no number multiple of 7 in a List.")