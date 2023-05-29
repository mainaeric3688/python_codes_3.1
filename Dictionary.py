'''
Python programming
Python program implemnting Dictionary in python collections

''' 
fruits=["Apples", "Oranges", "Banana", "Melon"]
for fruits in fruits:
    print(fruits)
students={
    "name":"Eric",
    "Reg_No":"BSCIT" ,
    "DOB": 2002
        }
a=students["name"]
print(a)
b=students.get("DOB")
print(b)
if "name" in students:
    print("Yes,name exists")
else:
    print("Doesn't exists")

    
    
    
    