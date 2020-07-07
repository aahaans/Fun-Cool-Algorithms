from sys import argv
from os import system
from math import sqrt

number = int(argv[1])
prime_numbers = []
prime_factors = []
_ = system('clear') 

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
	number /= prime_numbers[i]
	if number == 1:
		break

i = len(prime_factors)
j = 1

for k in prime_factors:
	if j == i:
		print(k)
		break

	print(k, end=" X ")
	j += 1