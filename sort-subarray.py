from sys import argv
from os import system

_ = system('clear')

if len(argv) < 2:
	print(f"Did You mean to add 'indivisual' or 'group'\n")

	print(f"'indivisual' -> It will take an array and multiple or single indices, it will the array ignoring the indices")
	print(f"'group' -> It will take 2 indices and ignore the indices between them and sort the rest of the array")
	exit()




if argv[1] == "indivisual":
	arr = input("Give an array: ")
	indices = input("Give Indices")
	indices = indices.split()
	print(indices)
	length_of_indices = len(indices)
	fixed_array = []
	output = []

	count = 0
	for i in range(len(arr) - 1):
		if count >= length_of_indices:
			break

		if i in indices:
			print(f"Skipped")
			count += 1
			continue

		fixed_array.append(arr[i])
		print(f"Added {arr[i]} to fixed_array")

	print(f"fixed_array before sorting = {fixed_array}")
	fixed_array = fixed_array.sort()
	print(f"fixed_array after sorting = {fixed_array}")

	for i in range(len(arr)):
		if i in indices:
			output.insert(i, indices[i])
			print(f"Added the not sorted {indices[i]}")

		output.insert(i, fixed_array[i])
		print(f"Added the sorted {fixed_array[i]}")


	print(f"The array {output} has been sorted the way you wanted")
