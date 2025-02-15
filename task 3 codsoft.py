import random
# take random letters, numbers, symbols which you want in your password
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+']

print("welcome to password generator")
# from here you can enter number of "letters","symbols","numbers" want to enter in your password
no_of_letters = int(input("How many letters you want in your password?\n"))
no_of_numbers = int(input("How many numbers you want in your password?\n"))
no_of_symbols = int(input("How many symbols you want in your password?\n"))

# taking a empty string
password=""
for i in range(1,no_of_letters+1):
    char = random.choice(letters)
    password = password + char # importing number's of letters in that empty string
for i in range(1,no_of_numbers+1):
    char = random.choice(numbers)
    password = password + char # importing number's of number in that empty string
for i in range(1,no_of_symbols+1):
    char = random.choice(symbols)
    password = password + char # importing number's of symbol in that empty string

print("Your generated password is: ",password) 