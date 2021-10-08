# Password Generator Project

import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
le = ""
for n in range(0, nr_letters):
    rand_letters = r.choice(letters)
    le += rand_letters

sy = ""
for n in range(0, nr_symbols):
    rand_symbols = r.choice(symbols)
    sy += rand_symbols
	
nu = ""
for n in range(0,nr_numbers):
    rand_numbers = r.choice(numbers)
    nu += rand_numbers

print("\nBasic password: \n")                                                   
print(le+sy+nu)

#more secure

str = le+sy+nu

str_list = list(str)

r.shuffle(str_list)

print("\nRandom password: \n")
for  n in range(0, len(str_list)):
    print(str_list[n], end="")
    
                                                                                                 
