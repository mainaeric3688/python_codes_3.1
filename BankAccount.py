# a python program using a class to perform bank operations
class BankAccount:

    def __init__(self, account_number, date_of_opening, balance=0):#the attributes
        self.account_number= account_number
        self.date_of_opening= date_of_opening
        self.balance=balance
      
    def deposit(self, deposited_amount):

        self.balance=+ deposited_amount

    def withdraw(self, deposited_amount):

        if self.balance>= deposited_amount:
            self.balance-= deposited_amount
                                                                             #the program vaidates if the amount to be withdrawn is sufficient from the available balamce in the a/c
        
        else:
            print("You have insufficient funds in your account ")

    def check_balance(self):

        return self.balance

    def customer_details(self):
        
        print("Name: MAINA ERIC N")
        print("Account number: 12345678")
        print("Acount opening date: 26/JUNE/2023")
        print("Account balance:Ksh 0")

amount=BankAccount(12345678,"26/JUNE/2023", balance=0)
print("The account details before any transaction is made is as follows:\n") 

print(amount.customer_details())
amount.deposit(9500)
print("The following transactions are then made:    \n  (a)Deposit of ksh 9500 into the account \n  (b)Withdrawal of ksh 4500 from the account  \n")

print("You have successfully deposited Ksh 9500 into your a/c ,\n   :new account balance is ksh", amount.check_balance())

amount.withdraw(4500)
print("You have successfully withdrawn Ksh 4500 from your a/c ,\n  :remaining account balance is ksh", amount.check_balance())


