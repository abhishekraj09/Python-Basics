student_marks={
    "jenny": 92,
    "harry": 82,
    "rahul":72

}
student_grade ={}
for student in student_marks:
    marks = student_marks[student]
    if marks>90:
        student_grade[student] ="A+"
    elif marks>80:
        student_grade[student] ="A"
    elif marks>70:
        student_grade[student]="B+"
    else:
        student_grade[student] = "F"
print(student_grade)