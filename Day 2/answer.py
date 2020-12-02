import re

# converts a file to an array of integers
# args : text file
def file_to_array(fname):
	f = open(fname, "r")

	array = []
	for line in f:
		stripped = line.strip()
		array.append(line.replace('\n', ''))

	f.close();
	return array

# checks occurences of a letter in a string, with min and max values
# args : string
def occurences(str):
	min_limit, max_limit, letter, code = re.findall(r'\w+', str)
	return (code.count(letter) >= int(min_limit)) and (code.count(letter) <= int(max_limit))

def indexes(str):
	first_index, second_index, letter, code = re.findall(r'\w+', str)
	return (code[int(first_index) - 1] == letter) ^ (code[int(second_index) - 1] == letter)

# returns count of valid items matching the password policy
def answer(func, array):
	return len(list(filter(func, input)))

input = file_to_array("input.txt")
print(answer(indexes, input))