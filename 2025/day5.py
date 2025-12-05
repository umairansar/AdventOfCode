file = "input_day5.txt"
ranges, ids = open(file).read().split("\n\n")
ranges, ids = ranges.split(), ids.split()
ranges = [list(map(int, ranje.split("-"))) for ranje in ranges]
ids = list(map(int, ids))
print(ranges, ids)

#Part 1
summ = 0
for i in ids:
	for l, r in ranges:
		if i >= l and i <= r:
			summ += 1
			break
print(summ)

#Part 2
buckets = []
ranges.sort(key=lambda x: x[0])
for l, r in ranges:
	new_bucket = []
	overlapping = False
	for bucket in buckets:
		# left overlap
		if l >= bucket[0] and l <= bucket[1] and r > bucket[1]:
			bucket[1] = r
			overlapping = True
			break
		# right overlap
		elif l < bucket[0] and r >= bucket[0] and r <= bucket[1]:
			bucket[0] = l
			overlapping = True
			break
		# subset
		elif l >= bucket[0] and r <= bucket[1]:
			overlapping = True
			break
		#superset
		elif l < bucket[0] and r > bucket[1]:
			bucket[0] = l
			bucket[1] = r
			overlapping = True
			break
	
	if not overlapping:
		buckets.append([l, r])
	 
[print(l, " -> ", r) for l, r in buckets]
good_ids = sum([h + 1 - l for l, h in buckets])
print(good_ids)
