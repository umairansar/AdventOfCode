
# part 1
listA = []
listB = []
with open("input_day1.txt") as file1:
	for line in file1:
		try:
			itemA, itemB = map(lambda x: int(x.strip()), line.split())
			listA.append(itemA)
			listB.append(itemB)
		except ValueError:
			pass

listA.sort()
listB.sort()

listPair = list(zip(listA, listB))

distance = 0
for a, b in listPair:
	distance += abs(a - b)

print(distance)

# part 2
similarityScore = 0
for item in listA:
	count = len(list(filter(lambda x: x==item, listB)))
	similarityScore += (item * count)

print(similarityScore)

input("press any key to exit")