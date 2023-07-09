#The super class for the python program
class Employee:
    def __init__(self,ID,Name):
        self.ID=ID
        self.Name=Name

#The second class (child) that is inherited from the super class Employee
class salaryEmployee(Employee):
    def __init__(self,ID,Name,basic_salary,allowance):
        self.basic_salary=basic_salary
        self.allowance=allowance
        super().__init__(ID,Name)

    def calculate_pay(self):
        pay=(self.basic_salary+self.allowance)
        return pay
#The third class(child) that inherits from the super class Employee
class HourlyEmployee(Employee):
    def __init__(self,ID,Name,Hours_worked,Hourly_pay):
       self.Hours_worked=Hours_worked
       self.Hourly_pay=Hourly_pay
       super().__init__(ID,Name)

    def calculate_payroll(self):
       payroll=5*(self.Hours_worked*self.Hourly_pay)
       return payroll

#The fourth class commissionEmployee that now inherites from salaryEmployee class
class commissionEmployee(salaryEmployee):
    def __init__(self,basic_salary,Name,ID,allowance,hours_worked):
        self.hours_worked=hours_worked
        super().__init__(basic_salary,allowance,ID,Name)

    def calculate_commission_pay(self): 
        if (int(self.hours_worked))>8:
            x=(self.hours_worked-8)  # x is the number of extra hours worked each day.The standard working hours for each day is 8 hours
            pay=4*5*x*300  #Therefore,each hour that excludes the company's standard working time which is 8,the extra hours obtained are multiplied by:
                                                     #Multiplied by: ksh 300 which is the pay for each extra hour worked and 5 working days in each week) 
                                                     #and 4(weeks per month) >pay=  4*5*x*300
            return pay  #returns the overall commission attained in that month
        elif (self.hours_worked>0 and self.hours_worked<8):
            pay=(250*self.hours_worked)
          
        else:
            pay=0
            return 0 

    def calculate_total_pay(self):
        if (self.hours_worked>8):
           x=(self.hours_worked-8)
           commission=int(4*5*x*300)
           total_pay=(commission+5000+35000)
           return total_pay
        elif (self.hours_worked>0 and self.hours_worked<8):
            pay=4*5*(hours_worked*250)
            return pay
        elif (self.hours_worked==8):
             pay=(0+35000+5000)
             return pay
        else:
              print("Invalid credential(s)") 
         
ID=int(input("Enter Employee's ID: "))
print("\nThe employee must work in accordance with either one of the following satisfactions: ")
print("  (a) Employee is to work at least 8 hours per day for 5 days a week.Any extra hour worked is credited as a commission and paid ksh 300 per hour.")
print("          Only For Employees working in monthly basis")
print("  (b) Working is flexible in such a way that suits the Employee.Each hour worked in the 5 working days is paid ksh 250 ")
print("          For Employees working in hourly pay.Payment done at the end of each week")
print("  (c) Incase the Employee working in monthly basis is either sick or in any situtuation of that kind,option (b) then takes over\n")
hours_worked=int(input("Enter the hours that the employee worked,daily: "))

#the objects
obj=Employee(ID,"MAINA ERIC")
obj_1=salaryEmployee(ID,"MAINA ERIC",35000,5000)
obj_2=HourlyEmployee(ID,"MAINA ERIC",hours_worked,250)
obj_3=commissionEmployee(ID,"MAINA ERIC",35000,5000,hours_worked)
obj_4=commissionEmployee(ID,"MAINA ERIC",35000,5000,hours_worked)

obj_1.calculate_pay()
obj_2.calculate_payroll()
obj_3.calculate_commission_pay()
obj_4.calculate_total_pay()

print("Employee details:\n   ID: "+str(ID) +"\n   Name: MAINA ERIC \n "+"  Basic salary: ksh 35000 \n"+"   Allowances: ksh 5000 ")    
print("The Employee's  monthly salary and allowances is ksh "+str(obj_1.calculate_pay()))
print("The total pay if the Employee worked in hourly pay, weekly is ksh "+str(obj_2.calculate_payroll()))
print("The commission the Employee  earned if he/she worked in monthly basis is ksh "+str(obj_3.calculate_commission_pay()))
print("The total income for the monthly employee is ksh "+str(obj_4.calculate_total_pay())+" in this month")
