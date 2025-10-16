n = list(map(int, input("enter the list of data:").split()))

ul = list(set(n))
ul.sort()
ndlr  = ul[-2]
print(ul)
print("the second largest number :",ndlr)