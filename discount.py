'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it
I love [rogramming in python
The program will assign the discountof 5% if the amount purchased exceeds 1000

'''
amount_purchased=int(input("Enter the amount purchased= sh"))
if amount_purchased>=1000:
    discount=amount_purchased*0.05
    print(discount)
    payable_amount=(amount_purchased-discount)
    print(payable_amount)
else:
    print("No discount allowed")
    print(amount_purchased)
      
