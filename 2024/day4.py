import sys,re

class Puzzle:
	def __init__(self):
		self.filename = "input_day4.txt"
		self.contents = []
		self.counter = 0
		self.__word = "XMAS"
		self.__word2 = "MAS"

	def extract(self):
		with open(self.filename) as file:
			self.contents = file.read().split()

	def reset(self):
		self.counter = 0

	def __inc(self):
		self.counter += 1

	def solve_part1(self, reverse=False):
		word = self.__word if not reverse else self.__word[::-1]
		print(word)

		#Check X at each spot, right and down
		for r, row in enumerate(self.contents):
			for c, val in enumerate(row):
				#Right case
				if val == word[0]:
					if not IsOutOfBound(len(row), c + 1) and row[c + 1] == word[1]:
						if not IsOutOfBound(len(row), c + 2) and row[c + 2] == word[2]:
							if not IsOutOfBound(len(row), c + 3) and row[c + 3] == word[3]:
								self.__inc()

				#Down case
				if val == word[0]:
					if not IsOutOfBound(len(self.contents), r + 1) and self.contents[r + 1][c] == word[1]:
						if not IsOutOfBound(len(self.contents), r + 2) and self.contents[r + 2][c] == word[2]:
							if not IsOutOfBound(len(self.contents), r + 3) and self.contents[r + 3][c] == word[3]:
								self.__inc()

				#Right Down
				if val == word[0]:
					if not IsOutOfBound(len(self.contents), r + 1) and not IsOutOfBound(len(row), c + 1) and self.contents[r + 1][c + 1] == word[1]:
						if not IsOutOfBound(len(self.contents), r + 2) and not IsOutOfBound(len(row), c + 2) and self.contents[r + 2][c + 2] == word[2]:
							if not IsOutOfBound(len(self.contents), r + 3) and not IsOutOfBound(len(row), c + 3) and self.contents[r + 3][c + 3] == word[3]:
								self.__inc()

				#Right Up
				if val == word[0]:
					if not IsOutOfBound(len(self.contents), r - 1) and not IsOutOfBound(len(row), c + 1) and self.contents[r - 1][c + 1] == word[1]:
						if not IsOutOfBound(len(self.contents), r - 2) and not IsOutOfBound(len(row), c + 2) and self.contents[r - 2][c + 2] == word[2]:
							if not IsOutOfBound(len(self.contents), r - 3) and not IsOutOfBound(len(row), c + 3) and self.contents[r - 3][c + 3] == word[3]:
								self.__inc()

	def solve_part2(self):
		commonAs = []
		word = self.__word2 
		wordReverse = self.__word2[::-1]

		for r, row in enumerate(self.contents):
			for c, val in enumerate(row):

				#Right Down
				if val == word[0]:
					if not IsOutOfBound(len(self.contents), r + 1) and not IsOutOfBound(len(row), c + 1) and self.contents[r + 1][c + 1] == word[1]:
						if not IsOutOfBound(len(self.contents), r + 2) and not IsOutOfBound(len(row), c + 2) and self.contents[r + 2][c + 2] == word[2]:
							commonAs.append((r+1, c+1)) #store A's ids
				#Right Up
				if val == word[0]:
					if not IsOutOfBound(len(self.contents), r - 1) and not IsOutOfBound(len(row), c + 1) and self.contents[r - 1][c + 1] == word[1]:
						if not IsOutOfBound(len(self.contents), r - 2) and not IsOutOfBound(len(row), c + 2) and self.contents[r - 2][c + 2] == word[2]:
							commonAs.append((r-1, c+1)) #store A's ids

				#Right Down
				if val == wordReverse[0]:
					if not IsOutOfBound(len(self.contents), r + 1) and not IsOutOfBound(len(row), c + 1) and self.contents[r + 1][c + 1] == wordReverse[1]:
						if not IsOutOfBound(len(self.contents), r + 2) and not IsOutOfBound(len(row), c + 2) and self.contents[r + 2][c + 2] == wordReverse[2]:
							commonAs.append((r+1, c+1)) #store A's ids
				#Right Up
				if val == wordReverse[0]:
					if not IsOutOfBound(len(self.contents), r - 1) and not IsOutOfBound(len(row), c + 1) and self.contents[r - 1][c + 1] == wordReverse[1]:
						if not IsOutOfBound(len(self.contents), r - 2) and not IsOutOfBound(len(row), c + 2) and self.contents[r - 2][c + 2] == wordReverse[2]:
							commonAs.append((r-1, c+1)) #store A's ids

		counterDict = {idx: commonAs.count(idx) for idx in commonAs}
		twosOrMore = [(x, y) for x, y in counterDict.items()]
		twosOrMore = list(filter(lambda x: x[1] == 2, twosOrMore))
		self.counter = len(twosOrMore)

def IsOutOfBound(listLength, idx):
	return idx < 0 or idx >= listLength

if __name__ == "__main__":
	puzzle = Puzzle()
	puzzle.extract()
	puzzle.solve_part1()
	puzzle.solve_part1(reverse=True)
	print("part1:", puzzle.counter)

	puzzle.reset()

	puzzle.solve_part2()
	print("part2:", puzzle.counter)
s
	# ws = []
	# with open('input_day4.txt', 'r') as f:
	# 	for line in f.readlines():
	# 		print(line)
	# 		ws.append([x for x in line if x != '\n'])
	# 		# print(ws)    		
	
	# with open("input_day4.txt") as file:
	# 	t = file.read()
	# 	w = t.index("\n")
	# 	print(sum(len(re.findall("(?s)(?=%s)" % (".{%d}" % offset).join(word), t))
	# 	    for word in ["XMAS", "SAMX"] for offset in [0, w+1, w, w-1]))