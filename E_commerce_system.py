 #The first function that takes the product name,price and quantity and return its dictionary
def add_product(dict):
    product={
        "Product name":"Milk",
        "Price":"55.25",
        "Quantity":"500 ml"
        }
    return (dict(product))

#The second function that takes product name,new price to be updated and quantity
#function returns new dictionary containing product name,updated price and the quantity
def update_price(price):
    new_product={
        "Product name":"Milk",
        "Price":str(new_price),
        "Quantity":"500 ml"
        }
    return (dict(new_product))
    
#The third function that takes product name,the updated price and the new quantity to modified also
#function returns new dictionary containing product name,updated price and quantity    
def update_quantity(quantity):
    new_product={
        "Product name":"Milk",
        "Price":str(new_price),
        "Quantity":str (new_quantity)+" ml"
        }
    return (dict(new_product))

print("~ Initial dictionary for the product details before updating it is: ")
print(add_product(dict))

#The user will be prompt to enter the new price so as to update the older one
new_price=float(input("Enter the new price to update:  "))
print(update_price(new_price))

#The user will be prompt to enter the new quantity so as to update the older one
new_quantity=int(input("Enter the new quantity to be modified:  "))
print(update_quantity(new_quantity)) 
