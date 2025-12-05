# part 1
def isSafe(report):
	# check for duplicates
	unique = set(report)
	counter = list(map(lambda key: report.count(key), unique))
	noDuplicate = all([x == 1 for x in counter])

	# either sort compares OR sort reverse compares
	sortPlain = sorted(report, reverse=False)
	sortReverse = sorted(report, reverse=True)
	strictOrdering = (report == sortPlain) or (report == sortReverse)

	# at most 3
	atMost3 = all([abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)])

	return noDuplicate and strictOrdering and atMost3

safeCount = 0

with open("input_day2.txt") as file:
	for report in file:
		report = list(map(lambda x: int(x.strip()), report.split()))
		# print(report)
		if isSafe(report):
			safeCount += 1
 
print(safeCount)

# part 2
def isAlmostStrictlyOrdered(report, reportSort):
	reportZip = zip(report, reportSort)
	difference = -1
	
	res = False
	for x, y in reportZip:
		if x != y:
			difference = y
			reportCopy = report[:]
			reportCopy.remove(difference)
			res = res or isSafe(reportCopy)

	if difference == -1:
		return isSafe(report)

	return res

def isAlmostNotHugeJump(report):
	indexesWithDifference = [(i, abs(report[i] - report[i + 1])) for i in range(len(report) - 1)]
	hasViolation = any([x[1] > 3 for x in indexesWithDifference])
	
	if hasViolation:
		violations = list(filter(lambda x: x[1] > 3, indexesWithDifference))
		reportCopyI, reportCopyIPlus1 = report[:], report[:]
		reportCopyI.pop(violations[0][0])
		reportCopyIPlus1.pop(violations[0][0] + 1)
		return isSafe(reportCopyI) or isSafe(reportCopyIPlus1)

	return False

def isAlmostSafe(report: list[str]) -> bool:
	uniqueReport = set(report)
	duplicates = (len(report) - len(uniqueReport))
	
	if duplicates > 1:
		return False
	
	elif duplicates == 1:
		duplicateItem, duplicateCount = list(filter(lambda x: x[1] > 1, list(map(lambda key: (key, report.count(key)), uniqueReport))))[0]
		reportCopyPlain, reportCopyReverse = report[:], report[::-1]
		reportCopyPlain.remove(duplicateItem)
		reportCopyReverse.remove(duplicateItem)
		return isSafe(reportCopyPlain) or isSafe(reportCopyReverse)

	return isAlmostStrictlyOrdered(report, sorted(report)) or isAlmostNotHugeJump(report)

almostSafeCount = 0

with open("input_day2.txt") as file:
	for report in file:
		report = list(map(lambda x: int(x.strip()), report.split()))
		if isAlmostSafe(report):
			almostSafeCount += 1

print(almostSafeCount)

input("Press any key to exit...")