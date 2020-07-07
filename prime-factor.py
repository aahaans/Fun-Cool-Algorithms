from sys import argv
from os import system, get_terminal_size
from math import sqrt
from time import sleep

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

for i in range(2, int(number)):
	if is_prime(i):
			prime_numbers.append(i)	

i = 0

while True:
	if (number % prime_numbers[i] != 0):
		i += 1
		continue
	
	prime_factors.append(prime_numbers[i])
	print("%2d  | %3d".center(width) % (prime_numbers[i], number))
	sleep(1)																# This line is optional and changable
	print("_________".center(width))
	sleep(1)																# This line is optional and changable
	number /= prime_numbers[i]
	if number == 1:
		break
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