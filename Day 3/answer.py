import math

def answer(input, iFactor, jFactor):
	i, j, count = 0, 0, 0
	
	while i < len(list(input)):
		# reset column item to start
		line = input[i]
		if j >= len(line):
			j = j - len(line)

		# checking tree
		if line[j] == '#' :
			count += 1
		
		j += jFactor
		i += iFactor
	
	return count


f = open("input.txt", "r")
input = [line.strip() for line in f.readlines() if line.strip()]

part1 = answer(input, 1, 3)
print("answer 1 :", part1)
part2 = [
	answer(input, 1, 1),
	answer(input, 1, 3),
	answer(input, 1, 5),
	answer(input, 1, 7),
	answer(input, 2, 1)
]
print("answer 2 :", math.prod(part2))