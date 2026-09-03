StudentName=input("Enter the name of the Student :")
USN=int(input("Enter the USN of the Student :"))
Branch=input("Enter the Branch of the Student :")
Semester=int(input("Enter the semester of the Student :"))
TotalMarks=0
for i in range(3):
    Marks=float(input("Enter the Mark of the Student :"))
    TotalMarks=TotalMarks+Marks
AverageMarks=TotalMarks/3
print("------------Student details------------")
print("NAME :",StudentName)
print("USN :",USN)
print("BRANCH :",Branch)
print("SEMESTER :",Semester)
print("TOTAl MARKS :",TotalMarks)
print("AVG MARKS {}".format(AverageMarks))
