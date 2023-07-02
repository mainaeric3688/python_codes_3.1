'''
 a python function to convert temperature to and from celsius to fahrenheit
'''
import math #import math package to help in rounding off the output into 1d.p


#the class in the program,named Temperature
class Temperature:
    
    def __init__(self,fahrenheit,celsius):
       self.fahreheit=fahrenheit
       self.celsius=celsius
       
#the first function to convert the temperature from celsius to fanrenheit
    def convertFahrenheit(self):
        f=((9/5*self.fahreheit)+32)
        x=math.ceil(1*f)/1
        return(x)
        
#the second function to convert the temperature to celsius from fanrenheit
    def convertCelsius(self):
        c=((5/9*self.celsius)-32)
        x=math.ceil(1*c)/1
        return(x)

    def validate_either_fahrenheit_or_celsius(s ): 
      if  s==1:
       print(Temperature.convertCelsius(t))
      elif s==2:
       print(Temperature.convertFahrenheit(t ))
      else :  
         print("!Invalid input for mode of conversion,choose either (1 or 2) " )

 #the program will propmt the user to input the value of the temperature to be converted
t=int(input("Enter the value of the temperature to be converted in either way ="))
print("\nThe value to be converted either from (F to C) or (C to F) is "+str(t))   

#more details on the conversion
print(" :Conversion of temperature to and from  Fahrenheit(F) to Celsius(C)  \n ")

#the object(s) of the class
temp1=Temperature(t,t)
temp2=Temperature(t,t)

p=(temp1.convertFahrenheit()) 
q=(temp2.convertCelsius())

#the program will execute and print the output
print(str(t)+" celsius(C)  = "+str(p)+(" Fahrenheit(F)"))
print(str(t)+"  Fahrenheit(F) = "+str(q)+(" celsius(C) "))
               
 

