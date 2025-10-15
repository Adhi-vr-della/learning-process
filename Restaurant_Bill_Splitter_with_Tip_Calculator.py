# input

total_amnt = float(input("Enter your total amount of the bill:"))
shares = int(input("Enter the number of shares the bill :"))
tip = int(input("Enter the tip amount :"))

# find the tip percentage
tip_amnt = total_amnt * tip /100


# find the total amount
bill_amnt = total_amnt + tip_amnt

# find the shares of each
shares_amnt = bill_amnt /shares


# output
print("The total amount of the bill include tip is ", round(bill_amnt),"$")
print(" how much each person should pay ", round(shares_amnt),"$")
