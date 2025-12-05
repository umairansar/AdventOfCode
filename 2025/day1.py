import time

class Command:
	def __init__(self, direction: str, magnitude: str):
		self.direction = direction
		self.magnitude = int(magnitude) % 100
		self.zero_ticks = int(magnitude) // 100

	def execute(self, current_position: int) -> int:
		if self.direction == "L":
			if self.__overflow(current_position):
				overflowing_magnitude = self.magnitude - current_position
				
				# part 2
				if current_position == 0:
					pass
				else:
					self.zero_ticks += 1
				
				return 100 - overflowing_magnitude
			return current_position - self.magnitude

		elif self.direction == "R":
			if self.__overflow(current_position):
				overflowing_magnitude = self.magnitude + current_position
				
				# part 2
				if overflowing_magnitude == 100:
					pass
				else:
					self.zero_ticks += 1
				
				return overflowing_magnitude - 100
			return current_position + self.magnitude

	def __overflow(self, current_position):
		if self.direction == "L":
			return current_position - self.magnitude < 0
		elif self.direction == "R": 
			return current_position + self.magnitude > 99

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return f"{self.direction}{self.magnitude}"


class SafeBox:
	def __init__(self):
		self.filename = "input_day1.txt"
		self.current_position = 50
		self.command_history = dict()
		self.commands = list()
		self.zero_ticks = 0
		self.__read_file()

	def __read_file(self):
		commands = open(self.filename).read().splitlines()
		[self.commands.append(Command(command[0], command[1:])) for command in commands]

	def unlock_safe(self):
		for idx, command in enumerate(self.commands):
			self.current_position = command.execute(self.current_position)
			key = str(command) + ":" + str(idx)
			self.command_history[key] = self.current_position

	def get_password(self):
		return list(self.command_history.values()).count(0)

	def get_password_0x434C49434B(self):
		allZeroStops = list(self.command_history.values()).count(0)
		allZeroPasses = sum([command.zero_ticks for command in self.commands])
		return allZeroStops + allZeroPasses


if __name__ == "__main__":
	start = time.time()
	s = SafeBox()
	s.unlock_safe()
	print(s.commands)
	print(s.command_history)
	print("Password 1: ", s.get_password())
	print("Password 2: ", s.get_password_0x434C49434B())
	end = time.time()
	print("Execution time:", round(end - start, 3), "s")