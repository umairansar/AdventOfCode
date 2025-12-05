class RuleChecker:

	def __init__(self):
		self.filename = "input_day5.1.txt"
		self.rules_raw = []
		self.rules = {}
		self.updates = []
		self.__prepare_input()
		self.__run_rule_compaction()

	def __prepare_input(self):
		with open(self.filename) as file:
			next_section = False
			for line in file:
				if line == "\n":
					next_section = True
					continue

				if next_section:
					self.updates.append(line.strip("\n").split(","))
				else:
					self.rules_raw.append(line.strip("\n"))

	def __get_rule_values(self, rule):
		return self.rules[rule[0]]+[rule[1]] if self.rules.get(rule[0]) != None else [rule[1]]

	def __get_rule_key(self, rule):
		return rule[0]

	def __run_rule_compaction(self):
		rulesList = list(map(lambda x: tuple(x.split("|")), self.rules_raw))
		# print(rulesList)
		[self.rules.update({self.__get_rule_key(rule) : self.__get_rule_values(rule)}) for rule in rulesList]

	def solve_part1(self):
		success = 0
		summa = 0
		for update in x.updates:
			violation = False
			for idx in range(1, len(update)):
				val = update[idx]
				to_be_checked = update[:idx]

				#check violation
				violations = [y for y in to_be_checked if x.rules.get(val) != None and y in x.rules.get(val)]
				if len(violations) > 0:
					# print("Violation for update ", update, " at rule val", val)
					violation = True
					break

			if not violation:
				success += 1
				summa += int(update[len(update) // 2])

		print(success, summa)

	def solve_part2(self):
		corrected = 0
		summa = 0
		for update in x.updates:
			violations_per_update = False
			update_corrected = update[:]
			for idx in range(1, len(update)):
				violation_per_rule = False
				val = update[idx]
				to_be_checked = update[:idx]

				#check violation
				violations = [y for y in to_be_checked if x.rules.get(val) != None and y in x.rules.get(val)]
				# print(violations)
				if len(violations) > 0:
					# print("Violation for update ", update, " at rule val", val)
					for violation in violations:
						update_corrected = list(filter(lambda x: x not in violations, update_corrected))
						val_idx = update_corrected.index(val)
						update_corrected = update_corrected[:val_idx+1] + violations + update_corrected[val_idx+1:]
					violation_per_rule = True
					violations_per_update = True
					# break

				if violation_per_rule:
					print("Before > ", update)
					update = update_corrected
					print("After > ", update)

			if violations_per_update:
				corrected += 1
				summa += int(update[len(update) // 2])

		print(corrected, summa)


class RuleChecker2:

	def __init__(self):
		self.filename = "input_day5.1.txt"
		self.data = ""
		self.rules = []
		self.updates = []
		self.__read_file()
		self.__run_rule_compaction()

	def __read_file(self):
		data = ""
		with open(self.filename) as file:
			blob = file.read().split("\n\n")
			self.rules = [rule.split("|") for rule in blob[0].split("\n")]
			self.updates = [update.split(",") for update in blob[1].split("\n")]

	def __run_rule_compaction(self):
		rules_compact = {}
		for k, v in self.rules:
			if rules_compact.get(k) == None:
				rules_compact[k] = set()
			rules_compact[k].add(v)
		self.rules = rules_compact

	def solve_part1(self):
		success = 0
		summa = 0
		for update in y.updates:
			relevant_rules = {key: value for key, value in y.rules.items() if key in update}
			valid = True
			for rule_key, rule_values, in relevant_rules.items():
				if not RuleChecker2.is_valid(rule_key, rule_values, update):
					valid = False
			
			if valid:
				success += 1
				summa += int(update[len(update) // 2])

		print(success, summa)

	def solve_part2(self):
		success = 0
		summa = 0
		for update in y.updates:
			relevant_rules = {key: value for key, value in y.rules.items() if key in update}
			valid_update = True
			for rule_key, rule_values, in relevant_rules.items():
				valid_for_rule = True
				if not RuleChecker2.is_valid(rule_key, rule_values, update):
					valid_update = False
					valid_for_rule = False

				if not valid_for_rule:
					update = self.__fix_update_for_rule(update, rule_key, rule_values)

			if not valid_update:
				success += 1
				summa += int(update[len(update) // 2])

		print(success, summa)

	def __fix_update_for_rule(self, update, rule_key, rule_values):
		val_idx = update.index(rule_key)
		to_be_moved = rule_values.intersection(update[:val_idx])
		update = list(filter(lambda x: x not in to_be_moved, update))
		val_idx = update.index(rule_key) # again becuase update was modified and idx could have changed
		return update[:val_idx+1] + list(to_be_moved) + update[val_idx+1:]

	@classmethod
	def is_valid(cls, rule_key, rule_values, update):
		val_idx = update.index(rule_key)
		if rule_values.intersection(update[:val_idx]):
			return False
		return True

if __name__ == "__main__":
	x = RuleChecker()
	x.solve_part1()
	x.solve_part2()

	y = RuleChecker2()
	y.solve_part1()
	y.solve_part2()