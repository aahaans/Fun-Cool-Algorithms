"""from sys import argv
from os import system, get_terminal_size
from math import sqrt

number = int(argv[1])
width = get_terminal_size().columns
prime_numbers = []
prime_factors = []
_ = system('clear')
print() 

def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False

	return True

if is_prime(number):
	print(f"It is a prime number \nIts only factors are 1 and itself \n1, {number}")
	exit()

x = len(str(number))
for i in range(2, int(sqrt(number))):
	if is_prime(i):
			prime_numbers.append(i)

			#print(f"found ")
#print(prime_numbers)

i = 0
while True:
	


	if (number % prime_numbers[i] != 0):
		i += 1
		continue
	
	prime_factors.append(prime_numbers[i])
	print("%2d  | %3d".center(width) % (prime_numbers[i], number))
	print("_________".center(width))								
	number /= prime_numbers[i]
	#print (f"i = {i}, prime_numbers[{i}] = {prime_numbers[i]}, number = {number}")

	if number == 1 or i > len(prime_numbers) - 1:
		break

#prime_factors.append(number)


print("1".center(width))

print("Answer ")

i = len(prime_factors)
j = 1

for k in prime_factors:
	if j == i:
		print(k)
		break

	print(f"{k}", end=" X ")
	j += 1
"""
from sys import argv
from os import system, get_terminal_size
from math import sqrt

number = int(argv[1])
width = get_terminal_size().columns
prime_numbers = []
prime_factors = []
_ = system('clear')
print() 

def is_prime(n):
  for i in range(2, int(sqrt(n))):
  	#print(f"Hello")
    if n % i == 0 :
    	return False

  return True

if is_prime(number):
  print(f"It is a prime number \nIts only factors are 1 and itself \n1, {number}")
  exit()

x = len(str(number))
limit = int(sqrt(number))
for i in range(2, limit + 1):
  if is_prime(i) and (i%number == 0):
  	prime_numbers.append(i)

print(prime_numbers)

i = 0
while True:
  if i == len(prime_numbers) - 1:
    # prime_factors.append(int(number))
    break
  print(f"i = {i}, number = {number} prime_numbers[{i}] = {prime_numbers[i]}")
  if (number % prime_numbers[i] != 0):
    i += 1
    continue
  prime_factors.append(prime_numbers[i])
  print("%2d  | %3d".center(width) % (prime_numbers[i], number))
  print("_________".center(width))                                
  number /= prime_numbers[i]

print("1".center(width))

print("Answer ")
i = len(prime_factors)
j = 1
for k in prime_factors:
  if j == i:
    print(k)
    break
  print(f"{k}", end=" X ")
  j += 1