'''
This is prrogramming in python
Grading system
A program to grade the marks for four subjects of a student
'''
Subject_1=int(input("Enter the marks of the first subject:  "))
Subject_2=int(input("Enter the marks of the second subject:  "))
Subject_3=int(input("Enter the marks for the third subject:  "))
Subject_4=int(input("Enter the marks for the fourth subject:  "))
#Checking and validatiung the entered mark(s)
if Subject_1<0 or Subject_1>100 or Subject_2<0 or Subject_2>100 or Subject_3<0 or Subject_3>100 or Subject_4<0 or Subject_4>100:
    print("Invalid credential(s)")
else:
 avg=((Subject_1+Subject_2+Subject_3+Subject_4)/4)     #Calculating the average of the four subjects
 print("The average score is = "+ str(avg))
 #Grading of the marks
avg=((Subject_1+Subject_2+Subject_3+Subject_4)/4)    #Calculating the average of the four subjects
if avg>=70 and avg<=100:
     print("Mean grade of  A")
elif avg>=60 and avg<=69:
    print("Mean grade of B")
elif avg>=50  and avg<=59:
    print("Mean grade of C")
elif avg>=40 and avg<=49:
    print("Mean garde of D") 
elif avg>=0 and avg<=39:
    print("Fail")
