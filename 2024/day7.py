from itertools import permutations, product
import math

class Puzzle:

	def __init__(self):
		self.ops = ["*", "+"]
		self.lines = self.__parse_file()

	def __parse_file(self):
		lines = open("input_day7.txt").read().splitlines()
		lines = list(map(lambda x: x.replace(":", "").split(), lines))
		lines = list(map(lambda x: list(map(int, x)), lines))
		[line.reverse() for line in lines]
		return lines

	def get_ops_combinitions_slow(self, size: int) -> list[str]:
		res = []
		for counter in range(0, ops_size + 1):
			ops_set = ["*"] * counter + ["+"] * (ops_size - counter)
			ops_set_pers = list(set(permutations(ops_set)))
			ops_set_pers = list(map(list, ops_set_pers))
			res.extend(ops_set_pers) 
		# print(res)
		return res

	def get_ops_combinitions_fast_part1(self, size: int) -> list[str]:
		ops = ["+", "*"]
		if size == 0: 
			return [[]]
		else:
			f = []
			sub_combos = self.get_ops_combinitions_fast_part1(size - 1)
			[f.append(["+"] + sub_combo) for sub_combo in sub_combos]
			[f.append(["*"] + sub_combo) for sub_combo in sub_combos]
			return f

	def get_ops_combinitions_fast_part2(self, size: int) -> list[str]:
		if size == 0: 
			return [[]]
		else:
			f = []
			sub_combos = self.get_ops_combinitions_fast_part2(size - 1)
			[f.append(["+"] + sub_combo) for sub_combo in sub_combos]
			[f.append(["*"] + sub_combo) for sub_combo in sub_combos]
			[f.append(["||"] + sub_combo) for sub_combo in sub_combos]
			return f

	"""
	total
	x
	+
	y
	*
	z
	Stack

	"""
	def solve_part1(self):
		total = 0
		cals = 0
		totals = []
		for line in self.lines:
			ops_combos = self.get_ops_combinitions_fast_part1(len(line) - 2)
			total = line.pop()
			for ops in ops_combos:
				line_copy = line[:]
				acc = line_copy.pop()
				while len(line_copy) > 0:
					op = ops.pop()
					a2 = line_copy.pop()
					if op == "+":
						acc = acc + a2
					else:
						acc = acc * a2

				if acc == total:
					cals += 1
					totals.append(total)
					break
		print(cals)
		print(sum(totals))

	def solve_part2(self):
		total = 0
		cals = 0
		totals = []
		for line in self.lines:
			ops_combos = self.get_ops_combinitions_fast_part2(len(line) - 2)
			total = line.pop()
			for ops in ops_combos:
				line_copy = line[:]
				acc = line_copy.pop()
				while len(line_copy) > 0:
					op = ops.pop()
					a2 = line_copy.pop()
					if op == "+":
						acc = acc + a2
					elif op == "*":
						acc = acc * a2
					elif op == "||":
						acc = int(str(acc) + str(a2))

				if acc == total:
					cals += 1
					totals.append(total)
					break
		print(cals)
		print(sum(totals))

# def get_ops_combinations(size: int):
# 	if size == 0:
# 		return [[]]
# 	smaller = get_ops_combinations(size - 1)
# 	result = []
# 	for seq in smaller:
# 		result.append(["+"] + seq)
# 		result.append(["*"] + seq)
# 	return result
# print(get_ops_combinitions(2))

# def gen_ops(opcount):
#     ops = ['*'] * opcount
#     final_ops = ['+'] * opcount
#     while ops != final_ops:
#         yield ops
#         for i in range(opcount):
#             carry = 1 if ops[i] == '+' else 0
#             ops[i] = '*' if ops[i] == '+' else '+'
#             if carry == 0:
#                 break
#     yield ops

def gen_ops_simple(opcount):
    for ops in product(["*", "+"], repeat=opcount):
        yield list(ops)

if __name__ == "__main__":
	p = Puzzle()
	p.solve_part1()
	p = Puzzle()
	p.solve_part2()
	print(p.get_ops_combinitions_fast_part2(3))

	
