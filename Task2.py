import random


letters = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m',
           'N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
digits = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','%','^','&','*','(',')','{','}','[',']','<','>','?','.',',']

n_letters = int(input('How many letters do you want in your password?: '))
n_digits = int(input('How many digits do you want in your password?: '))
n_symbols = int(input('How many symbols do you want in your password?: '))
password = ""

for i in range(n_letters):
    char = random.choice(letters)
    password += char

for i in range(n_digits):
    digit = random.choice(digits)
    password += digit

for i in range(n_symbols):
    sym = random.choice(symbols)
    password += sym

# Convert the password into a list and shuffle it to ensure randomness
password_list = list(password)
random.shuffle(password_list)

# Join the list back into a string
password = ''.join(password_list)

# Print the generated password
print("Your password is:", password)
print("Thank you!")
