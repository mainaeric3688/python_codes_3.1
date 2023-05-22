'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it
I love [rogramming in python
The program will prompt he use to enter the user's age and Nationality
and check if they are eligible to vote

'''
age=int(input("Enter your age="))
citizenship=(input("Enter your citizenship="))
country=["kenya","uganda","tanzania"]
if age>=18 and citizenship.lower()in country:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
      
