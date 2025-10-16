n = list(map(int, input("Enter your list:").split()))

print("_____THE POSITIVE NUMBER IN THE LIST________")

for i in n:
    if i <0:
        continue
    print(i)