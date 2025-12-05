def in_range(row, col, grid):
	x_min, y_min = 0, 0
	x_max, y_max = len(grid) - 1, len(grid[0]) - 1
	return row >= x_min and row <= x_max and col >= y_min and col <= y_max

deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
grid = open("input_day4.txt").read().splitlines()
print(grid)

#Part 1
neighbour_counter = dict()
for row in range(len(grid)):
	for col in range(len(grid[0])):
		neighbours = [(row + delta[0], col + delta[1]) for delta in deltas]
		valid_neighbours = list(filter(lambda x: in_range(x[0], x[1], grid), neighbours))
		paper_neighbours = [1 for neighbour in valid_neighbours if grid[neighbour[0]][neighbour[1]] == "@"]
		if grid[row][col] == "@":
			neighbour_counter[(row, col)] = sum(paper_neighbours)

print(neighbour_counter)
# [print(str(k) + " -> " + str(v)) for k, v in neighbour_counter.items() if v < 4]
print(len([v for k, v in neighbour_counter.items() if v < 4]))

#Part 2
can_remove = True
total_removed = 0
grid = [list(row) for row in grid]
while can_remove:
	print("Round (total removed)", total_removed)
	neighbour_counter = dict()
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			neighbours = [(row + delta[0], col + delta[1]) for delta in deltas]
			valid_neighbours = list(filter(lambda x: in_range(x[0], x[1], grid), neighbours))
			paper_neighbours = [1 for neighbour in valid_neighbours if grid[neighbour[0]][neighbour[1]] == "@"]
			if grid[row][col] == "@":
				neighbour_counter[(row, col)] = sum(paper_neighbours)

	to_be_removed = len([v for k, v in neighbour_counter.items() if v < 4])
	if to_be_removed > 0:
		for k, v in neighbour_counter.items():
			if v < 4: 
				grid[k[0]][k[1]] = "."
		total_removed += to_be_removed
	else:
		can_remove = False

print(total_removed)