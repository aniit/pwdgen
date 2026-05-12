import string
import random

letters = []
for a in string.ascii_lowercase:
    letters.append(a)


for b in string.ascii_uppercase:
    letters.append(b)

numbers = []
for c in range(1,101):
    numbers.append(c)

symbols = ['!','#','$','%','(',')','*','+']

print('Welcome to the Password Generator!')
n_letters = int(input('Please enter the number of letters you want in your password: '))
n_numbers = int(input('Please enter the number of numbers you want in your password: '))
n_symbols = int(input('Please enter the number of symbols you want in your password: '))

l = random.choices(letters, k = n_letters)
m = random.choices(numbers, k = n_numbers)
n = random.choices(symbols, k = n_symbols)

print(l)
print(m)
print(n)

pass1 = l + m + n
print(pass1)
random.shuffle(pass1)
print(type(pass1))
print(pass1)

result = ''.join(map(str, pass1))

print(f'Heres your password :  {result}')


      


