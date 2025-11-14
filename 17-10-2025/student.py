student={"Name":"Ansha","Roll No":10,"Register Number":"MCA10","Department":"Computer Application","Semester":1}
print(student)
total_mark=int(input("Enter the total mark of the student: "))
student.update({"total_mark":total_mark})
mark=student["total_mark"]
if total_mark >=90:
    grade="A"
elif mark >=82:
    grade="B"
elif mark >=75:
    grade="C"
elif mark >=60:
    grade="D"
elif mark >=50:
    grade="P"
student.update({"grade":grade})
print(student)
del student["Roll No"]
print(student)
