def calculate_grade(score):
    if 80 <= score <= 100:
        # print("A")
        return "A"
    elif 70 <= score < 80:
        # print("B")
        return "B"
    elif 60 <= score < 70:
        # print("C")
        return "C"
    elif 50 <= score < 60:
        # print("D")
        return "D"
    elif 0 <= score < 50:
        # print("F")
        return "F"
    else:
        return "score error"
        # print("score error")


my_grade1 = calculate_grade(30)
my_grade2 = calculate_grade(50)
my_grade3 = calculate_grade(70)
print(my_grade1, my_grade2, my_grade3)
