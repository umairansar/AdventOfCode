import re


result: int = 0
do = True
with open("input_day3.txt") as file:
	for line in file:
		commands = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
		print(commands)
		for command in commands:
			if command == "do()":
				do = True
				continue
			
			if command == "don't()":
				do = False
				continue
			
			if do:
				var = command.split(",")
				x = var[0].strip("mul(")
				y = var[1].strip(")")
				result += int(x) * int(y)

print(result)