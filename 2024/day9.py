import time

class Disk:
	def __init__(self):
		self.filename = "input_day9.txt"
		self.disk = list()
		self.compacted_disk = list()
		self.mapping = list()
		self.__parse_file()

	def __parse_file(self):
		contents = open(self.filename).readlines()
		self.mapping = list(contents[0].strip())

	def traverse_mapping(self):
		for result in self.__step_next():
			self.disk.extend(result)
		self.compacted_disk = self.disk[:]

	def __step_next(self):
		free_space = False
		self.file_id = 0
		for value in self.mapping:
			if not free_space:
				yield [str(self.file_id)] * int(value)
				self.file_id += 1
			else:
				yield ["."] * int(value)
			free_space = not free_space

	def compact(self, debug_mode: bool):
		if debug_mode:
			print(f"Running Compaction... \n{''.join(self.compacted_disk)}")
		while self.__can_compact_fast():
			idx, file_id = self.__get_slot_to_move_fast()
			self.compacted_disk[idx] = "."
			new_idx = self.__get_first_free_slot()
			self.compacted_disk[new_idx] = file_id
			if debug_mode:
				print(''.join(self.compacted_disk))

	def __can_compact(self):
		right_most_file_id = list(filter(lambda x: x != ".", self.compacted_disk))[-1]
		right_most_file_idx = len(self.compacted_disk) - 1 - self.compacted_disk[::-1].index(right_most_file_id)
		left_most_empty_idx = self.compacted_disk.index(".")
		return right_most_file_idx > left_most_empty_idx

	def __can_compact_fast(self):
		for idx in range(len(self.compacted_disk) - 1, -1, -1):
			if self.compacted_disk[idx] != ".":
				left_most_empty_idx = self.compacted_disk.index(".")
				return idx > left_most_empty_idx
		return False		

	def __get_slot_to_move(self):
		file_id = list(filter(lambda x: x != ".", self.compacted_disk))[-1]
		idx = len(self.compacted_disk) - 1 - self.compacted_disk[::-1].index(file_id)
		return idx, file_id

	def __get_slot_to_move_fast(self):
		for idx in range(len(self.compacted_disk) - 1, -1, -1):
			if self.compacted_disk[idx] != ".":
				return idx, self.compacted_disk[idx]

	def __get_first_free_slot(self):
		return self.compacted_disk.index(".")

	def calculate_checksum(self):
		checksum_list = [int(idx) * int(value) if value != "." else 0 for idx, value in enumerate(self.compacted_disk)]
		return sum(checksum_list)

	def __str__(self):
		return f"Original Disk  : {''.join(self.disk)}\nCompacted Disk : {''.join(self.compacted_disk)}"

if __name__ == "__main__":
	start = time.time()
	disk = Disk()
	print(disk.mapping)
	disk.traverse_mapping()
	print(disk)
	disk.compact(False)
	print(disk)
	print("Checksum: ", disk.calculate_checksum())
	end = time.time()
	print("Execution time:", round(end - start, 3), "s")