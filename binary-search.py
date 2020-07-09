from sys import argv
from os import system

_ = system('clear')

arr = input("Give an array: ")						# You can replace it With an argv
arr = arr.split()
x = input("Give a number in from that array: ")		# You can replace it with an argv	

y = len(arr) - 1
#print(y)
t = y
#print(t)

in_array = False
count = 0

while t > 0:
	t = int(t / 2)
	#print(f"t = {t}")
	count += 1

	if int(arr[int(y)]) > int(x):
		y -= t
		#print(f"{arr[y]} greater than {x}")
	else :
		y += t
		#print(f"{arr[y]} less than {x}")

print()

print(f"The index with value {x} is {y} starting from 0 in the array -> \n{arr}")
print(f"This Search only took {count} rounds \n{max(y - count, 0)} Less than Linear Search")

