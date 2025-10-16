import statistics

def find_highest_mark(students):
    return max(students,key = lambda x: statistics.mean(students[x]))

def find_class_average(students):
    all_marks = [mark for marks in students.values() for mark in marks]
    return statistics.mean(all_marks)
