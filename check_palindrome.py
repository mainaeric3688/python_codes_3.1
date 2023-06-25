# Program to check if a string is palindrome or not
my_str = 'eye'
# make it suitable for caseless comparison
my_str = my_str.casefold()
# reverse the string
rev_str = reversed(my_str)
# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string 'eye' is a palindrome.")
else:
   print("The string  'eye' is not a palindrome.")# Program to check if a string is palindrome or not
my_str = 'book'
# make it suitable for caseless comparison
my_str = my_str.casefold()
# reverse the string
rev_str = reversed(my_str)
# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string 'book' is a palindrome.")
else:
   print("The string 'book' is not a palindrome.")
