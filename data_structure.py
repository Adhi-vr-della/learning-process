# data input
data  = list(map(str,input("Enter the students data (Name,Sub_name, ob_mark):").split()))

tup= []     #tuple is created


for i in data:   #loop for append list of datas into tuple where created

    records = i.split(",")     # help to split the list by ","
    name = records[0]          # 1st data of the list "name" as string
    sub_name = records[1]      # 2nd data from the list "subject name" as a string
    ob_mark = int(records[2])  # convert's the 3rd data as a string to integer
    tup.append((name,sub_name,ob_mark))    #it will append the data in each iteration  tuple where create

stu_dict = {}                          # dictionary has been created
for name,sub_name,ob_mark in tup:      # loop for travel into tup
    if name not in stu_dict:           # the dict doesn't contain a name, the name will be added as a key
        stu_dict[name] = {}            # initially the created dictionary is empty

    stu_dict[name][sub_name] = ob_mark  # it will map the values based on the key like map the mark for the name of the student

avg=0                                       #Global value
top_stu = ""                                #initalize the variable
top_avg = 0
print("Average Score of each student:")     #header
for name,sub_name in stu_dict.items():      #loop to get the student marks
    sc = sub_name.values()                  #variable that contain the number of subject by the student
    avg = sum(sc)/len(sc)                   #to find the average
    print(f'{name} :{round (avg, 2)}')

    if avg > top_avg:                       #condition to find the top average
        top_avg = avg                       #for update
        top_stu = name

subject = set()                             #set created


for name,sub_name,ob_mark in tup:           #loop to get the subjects
    subject.add(sub_name)
sorted_subject = sorted(subject)             #to sort the subjects by ascending order
jt = "|".join(sorted_subject)



#print statement


print("The unique subjects are:")
print(sorted(subject))
print(f'The top student is: {top_stu} ({round(top_avg, 2)})')
print("Students name(upper case):",[name.upper() for name in stu_dict.keys()])
print("Subjects:",jt.capitalize())
