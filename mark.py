s= {
    "Adhithyan": 85,
    "Priya": 92,
    "Rahul": 76,
    "Sneha": 89,
    "Karthik": 70
}
print(" Total student list:",s)


total_score = 0

for i in s:
    total_score += s[i]
    
avg = total_score / len(s)

print("The Average score:",avg)

print("The Students scoring above average:")
for j in s:
    if s[j] > avg:
        print(j)
        
print("The maximum score is =" ,s[max(s)])
print("The minimum score is =", s[min(s)])
    
    
