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
       payroll=(self.Hours_worked*self.Hourly_pay*5)  #5 is the number of working days per week
       return payroll

#The fourth class commissionEmployee that now inherites from salaryEmployee class
class commissionEmployee(salaryEmployee):
    def __init__(self,basic_salary,Name,ID,allowance,hours_worked):
        self.hours_worked=hours_worked
        super().__init__(basic_salary,allowance,ID,Name)

    def calculate_commission_pay(self): 
        if (int(self.hours_worked))>8:
            x=(self.hours_worked-8)
            pay=(x*250)*5*4    #the product of ksh 250 which is the pay for each hours that exclude the standard working hours of 8,(x)
                                              #5 is the number of days per week worked and 4 is the number of weeks per month worked
            return  pay
        else:
            pay=(0)
            return  pay

#the objects
obj=Employee(12345678,"MAINA ERIC")
obj_1=salaryEmployee(12345678,"MAINA ERIC",35000,5000)
obj_2=HourlyEmployee(12345678,"MAINA ERIC",10,250)
obj_3=commissionEmployee(12345678,"MAINA ERIC",35000,5000,10)

obj_1.calculate_pay()
obj_2.calculate_payroll()
obj_3.calculate_commission_pay

print("Employee details:\n   ID:12345678\n   Name:MAINA ERIC" )    
print("The Employee's total monthly salary and allowances is ksh "+str(obj_1.calculate_pay()))
print("The Employee's income if he/she worked in hourly pay, weekly is ksh "+str(obj_2.calculate_payroll()))
print("The commission earned by the Employee working in monthly basis is ksh "+str(obj_3.calculate_commission_pay()))

 
