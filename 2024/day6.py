GUARDS = {
	"^": (-1, 0), 
	"V": (+1, 0), 
	">": (0, +1), 
	"<": (0, -1)
	}

NEXT = {
	"^":">",
	">":"V",
	"V":"<",
	"<":"^" 
	}

class Guard:
	def __init__(self, x: int, y: int, direction: str):
		self.x = x
		self.y = y
		self.direction = direction

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return f"({self.x},{self.y}){self.direction}"

class HistoricalDay:
	def __init__(self):
		self.filename = "input_day6.1.txt"
		self.map = []
		self.guard = ""
		self.freeze_time = False
		self.route_unique = set()
		self.route_2 = set()
		self.obstacles = []
		self.__read_file()

	def __read_file(self):
		with open(self.filename) as file:
			for line_idx, line in enumerate(file):
				line = line.strip("\n")
				self.map.append(line)
				if set(GUARDS.keys()).intersection(line):
					guard_idx, direction = self.__find_guard_at_start(line)
					self.guard = Guard(line_idx, guard_idx, direction)
					self.route_unique.add((self.guard.x, self.guard.y))
					self.route_2.add((self.guard.x, self.guard.y, self.guard.direction))

	def __find_guard_at_start(self, line):
		for g in GUARDS:
			if g in line:
				return line.index(g), g

	def walk_path(self):
		while not self.freeze_time:
			self.__take_step()

		print("Ending simulation of historical day in 1518")

	def walk_path_loops(self):
		seen_states = set()
		while not self.freeze_time:
			state = (self.guard.x, self.guard.y, self.guard.direction)
			if state in seen_states:
				return True
			seen_states.add(state)
			self.__take_step()

		return False

	def __take_step(self):
		current_position = self.guard
		match self.guard.direction:
			case "^":
				new_position = current_position.x - 1, current_position.y
				self.__update_guard_position(new_position, ">")

			case ">":
				new_position = current_position.x, current_position.y + 1
				self.__update_guard_position(new_position, "V")

			case "<":
				new_position = current_position.x, current_position.y - 1
				self.__update_guard_position(new_position, "^")

			case "V":
				new_position = current_position.x + 1, current_position.y
				self.__update_guard_position(new_position, "<")

	def __update_guard_position(self, new_position, direction):
		if self.is_moving_out(new_position[0], new_position[1]):
			self.freeze_time = True
		elif self.is_hitting_obstacle(new_position[0], new_position[1]):
			self.guard.direction = direction
			self.obstacles.append((new_position[0], new_position[1]))
		else:
			self.guard.x, self.guard.y = new_position[0], new_position[1]
			self.route_unique.add((self.guard.x, self.guard.y))
			self.route_2.add((self.guard.x, self.guard.y, self.guard.direction))

	def is_moving_out(self, x, y):
		return x < 0 or x >= len(self.map) or y < 0 or y >= len(self.map[0])

	def is_hitting_obstacle(self, x, y):
		return self.map[x][y] in ["#", "O"]

	def has_obstacle_in_direction(self, current_pos, direction):
		match direction:
			case "^":
				pathway = self.map[current_pos[0]]
				return any([pathway[x] in ["#", "O"] for x in range(current_pos[1] + 1, len(pathway))])
			case ">":
				pathway = [row[current_pos[1]] for row in self.map]
				return any([pathway[x] in ["#", "O"] for x in range(current_pos[0] + 1, len(pathway))])
			case "<":
				pathway = [row[current_pos[1]] for row in self.map]
				return any([pathway[x] in ["#", "O"] for x in range(0, current_pos[0])])
			case "V":
				pathway = self.map[current_pos[0]]
				return any([pathway[x] in ["#", "O"] for x in range(0, current_pos[1])])

def run_simulation(day, x, y, direction, possible_obstacles):
	x0, y0 = x, y
	dx, dy = GUARDS[direction]
	x, y = x + dx, y + dy

	# next step case
	if not day.is_moving_out(x, y) and not day.is_hitting_obstacle(x, y):
		day.map[x] = day.map[x][:y] + "O" + day.map[x][y + 1:]
		if day.walk_path_loops():
			possible_obstacles.add((x, y))
	
	# corner case
	else:
		x, y = x0, y0
		dx, dy = GUARDS[NEXT[direction]]
		x, y = x + dx, y + dy
		if not day.is_moving_out(x, y) and not day.is_hitting_obstacle(x, y):
			day.map[x] = day.map[x][:y] + "O" + day.map[x][y + 1:]
			if day.walk_path_loops():
				possible_obstacles.add((x, y))

if __name__ == "__main__":
	day = HistoricalDay()
	starting_pos = (day.guard.x, day.guard.y, day.guard.direction)

	day.walk_path()
	print(len(day.route_unique))

	path = set(day.route_2) - {starting_pos}

	print(day.has_obstacle_in_direction((5, 6), ">"))
	print(day.route_2)
	print(len(day.route_unique))
	print(len(day.route_2))
	
	# Try putting obstacle in each path
	possible_obstacles = set()
	for pos in path:
		day = HistoricalDay()
		x, y = pos[0], pos[1]
		match pos[2]:
			case "^":
				run_simulation(day, x, y, "^", possible_obstacles)

			case ">":
				run_simulation(day, x, y, ">", possible_obstacles)

			case "<":
				run_simulation(day, x, y, "<", possible_obstacles)

			case "V":
				run_simulation(day, x, y, "V", possible_obstacles)

	print(possible_obstacles)
	print(len(possible_obstacles))
