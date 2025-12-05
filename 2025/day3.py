class Bank:
	def __init__(self, bank):
		self.bank = list(map(int, list(bank)))
		self.left_peak = None
		self.right_peak = None
		self.super_joltage = None

	def calculate_peak_joltage(self):
		self.left_peak = 0
		self.right_peak = len(self.bank) - 1

		l_peak_idx = 0
		l_peak_val = 0
		for i in range(len(self.bank) - 1):
			# print(i, self.bank[i], l_peak_val)
			if self.bank[i] > l_peak_val:
				l_peak_val = self.bank[i]
				l_peak_idx = i
		self.left_peak = l_peak_val

		# print("Found l peak ", self.left_peak, "at idx", l_peak_idx)

		r_peak_idx = 0
		r_peak_val = 0
		for j in range(len(self.bank) -1, l_peak_idx, -1):
			# print(j, self.bank[j], r_peak_val)
			if self.bank[j] > r_peak_val:
				r_peak_val = self.bank[j]
				r_peak_idx = j
		self.right_peak = r_peak_val

	def calculate_super_peak_joltage(self):
		l_peak_idx = 0
		l_peak_val = 0

		# find peak with at least 11 places on right:
		for i in range(len(self.bank) - 11):
			if self.bank[i] > l_peak_val:
				l_peak_val = self.bank[i]
				l_peak_idx = i
		# print("Found l peak ", l_peak_val, "at idx", l_peak_idx)
		
		peaks_idx = [l_peak_idx] + [0] * 11
		peaks_val = [l_peak_val] + [0] * 11

		# print("peaks_idx", peaks_idx)
		# print("peaks_val", peaks_val)
		
		# find peak with at least i places on right:
		for i in range(1, 12):
			print(peaks_idx[i - 1])
			for j in range(peaks_idx[i - 1] + 1, len(self.bank) - (11 - i)):
				if self.bank[j] > peaks_val[i]:
					peaks_val[i] = self.bank[j]
					peaks_idx[i] = j

		# print("peaks_idx", peaks_idx)
		# print("peaks_val", peaks_val)
		self.super_joltage = peaks_val

	@property
	def joltage_rating(self):
		if self.left_peak == None or self.right_peak == None:
			return -1
		return int(str(self.left_peak) + str(self.right_peak))

	@property
	def super_joltage_rating(self):
		if self.super_joltage == None:
			return -1
		return int("".join(list(map(str, self.super_joltage))))
	

if __name__ == "__main__":
	file = "input_day3.txt"
	s_banks = open(file).read().splitlines()
	print(s_banks)
	banks = [Bank(bank) for bank in s_banks]

	for bank in banks:
		bank.calculate_peak_joltage()
	joltages = [bank.joltage_rating for bank in banks]
	print("p1: joltages:", joltages)
	print("p1: joltages sum:", sum(joltages))

	for bank in banks:
			bank.calculate_super_peak_joltage()
	joltages = [bank.super_joltage_rating for bank in banks]
	print("p2: joltages:", joltages)
	print("p2: joltages sum:", sum(joltages))
	

