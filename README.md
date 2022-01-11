# simple password generator
import random
input_alphabets = int(input("Enter the number of letters you want: "))
input_numbers = int(input("Enter the total numbers you want: "))
input_char = int(input("Enter the total number of symbols you want: "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random1 = ['s','n','l']
a = input_alphabets
n = input_numbers
c = input_char
p = ""
x = ""
y= ""
length = a + n + c
password = ""
for y in range(0,length):
    x = random.choice(random1)
    if x == 'l' and input_alphabets == 0:
        random1.pop(random1.index('l'))
    elif x == 'n' and input_numbers == 0:
        random1.pop(random1.index('n'))
    elif x == 's' and input_char == 0:
        random1.pop(random1.index('s'))
    elif x == 'l' and input_alphabets>0:
        input_alphabets -=1
        p = random.choice(letters)
        password += p
        p=""
        if input_alphabets==0:
            random1.pop(random1.index('l'))
    elif x == 'n' and input_numbers>0:
        input_numbers -=1
        p = random.choice(numbers)
        password += p
        p=""
        if input_numbers==0:
            random1.pop(random1.index('n'))
    elif x == 's' and input_char>0:
        input_char -= 1
        p = random.choice(symbols)
        password += p
        p = ""
        if input_char==0:
            random1.pop(random1.index('s'))
print(password)
