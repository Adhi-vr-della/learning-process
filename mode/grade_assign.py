def calculate_avg(marks):
    avg = sum(marks) / len(marks)
    return avg


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80 and avg < 89 :
        return "B"
    elif avg >= 70 and avg < 79 :
        return "C"
    elif avg >= 60 and avg < 69 :
        return "D"
    elif avg >= 50 and avg < 50 :
        return "E"
    else:
        return "F"