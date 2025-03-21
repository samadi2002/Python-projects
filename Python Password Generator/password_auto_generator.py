#Password auto-generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword AutoGenerator!")
print("Here is Your password!")

password_list = []

for letter in range(0,random.randint(2,4)):
    random_letters = random.choice(letters)
    password_list.append(str(random_letters))

for symbol in range(0,random.randint(2,4)):
    random_symbols = random.choice(symbols)
    password_list.append(str(random_symbols))

for number in range(0, random.randint(2,4)):
    random_numbers = random.choice(numbers)
    password_list.append(str(random_numbers))
random.shuffle(password_list)
f_password = "".join(password_list)
print(f_password)