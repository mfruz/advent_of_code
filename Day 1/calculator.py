# converts a file to an array of integers
# args : text file
def file_to_array(fname):
	f = open(fname, "r")

	input = []
	for line in f:
		stripped = line.strip()
		input.append(int(line.replace('\n', '')))

	f.close();
	return input


# finds 2 ints that add to 2020 and multiply them
# args : array of ints
def first_puzzle(array):
	for x in array:
		for y in array:
			if((2020 - x) == y):
				# print(x)
				# print(y)
				return x * y

# finds 3 ints that add to 2020 and multiply them
# args : array of ints
def second_puzzle(array):
	for x in array:
		for y in array:
			for z in array:
				if(x + y + z == 2020):
					# print(x)
					# print(y)
					# print(z)
					return x * y * z

# main function
def main():
	input = file_to_array("input.txt")

	print(first_puzzle(input))
	print(second_puzzle(input))

# executing main
main()