 # a python program using a class to perform bank operations
class BankAccount:

    def __init__(self, account_number, date_of_opening, balance=0):#the attributes
        self.account_number= account_number
        self.date_of_opening= date_of_opening
        self.balance=balance
      
    def deposit(self, deposited_amount):

        self.balance=+ deposited_amount

    def withdraw(self, withdraw_amount):

        if self.balance>= withdraw_amount:
            self.balance-= withdraw_amount
            print("You hasve successfully withdrawn Ksh "+str(withdraw_amount)+" from your a/c ,\n  new account balance is ksh", amount.check_balance())
#the program validates if the amount to be withdrawn is sufficient from the available balance in the a/c
        else:
            print("Failed! You have insufficient funds in your account to complete the transaction.")
            print("    Your account balance is ksh " +str(self.balance)+" ,Please recharge your account and try again")  

    def check_balance(self):

        return self.balance

    def customer_details(self):
        
        print(" ~ Name: MAINA ERIC N")
        print(" ~ Account number: 12345678")
        print(" ~ Acount opening date: 10/JULY/2023")
        print(" ~ Account balance:Ksh 0")

amount=BankAccount(12345678,"10/JULY/2023", balance=0)
print("The account details are as follows:") 
print(amount.customer_details())

dep=float(input("Enter the amount to be deposited,ksh "))
amount.deposit(dep)

print("You have successfully deposited Ksh "+str(dep)+" into your a/c ,\n   new account balance is ksh", amount.check_balance())

withdraw_amount=float(input("Enter the amount to be withdrawn,ksh "))
amount.withdraw(withdraw_amount)




 
