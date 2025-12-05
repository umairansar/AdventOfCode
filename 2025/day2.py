import time

class Range:
	def __init__(self, low, high):
		self.low = low.strip()
		self.high = high.strip()
		self.violations_1 = []
		self.violations_2 = set()

	def find_violations_1(self):
		ptr = int(self.low)
		high = int(self.high) + 1 
		while ptr != high:
			s_ptr = str(ptr)
			mid = len(s_ptr) // 2
			left = s_ptr[0:mid]
			righ = s_ptr[mid:]
			if left == righ:
				self.violations_1.append(ptr)
			ptr += 1
		return self.violations_1

	def find_violations_2_stupid(self):
		ptr = int(self.low)
		high = int(self.high) + 1 
		while ptr != high:
			divider = 2
			s_ptr = str(ptr)
			while len(s_ptr) // divider != 0:
				if len(s_ptr) // divider != len(s_ptr) / divider:
					divider += 1
					continue
				mid = len(s_ptr) // divider
				chunks = [s_ptr[i*mid:(i+1)*mid] for i in range(divider)]
				print(chunks)
				if len(set(chunks)) == 1:
					self.violations_2.append(ptr)
					break
				divider += 1
			ptr += 1
		return self.violations_2

	def __init_buckets(self, s_ptr):
		len_ptr = len(s_ptr)
		dividers = list(filter(lambda x: len_ptr // x == len_ptr / x, list(range(2, len_ptr + 1))))
		buckets = dict()
		for divider in dividers:
			slot_size = len(s_ptr) // divider
			for i in range(divider):
				new_bucket = int(s_ptr[i*slot_size:(i+1)*slot_size])
				if buckets.get(divider) != None:
					buckets[divider][0].append(new_bucket)
				else:
					buckets[divider] = [[new_bucket], slot_size]

		return buckets

	def find_violations_2_fast(self):
		ptr = int(self.high)
		low = int(self.low)

		s_ptr = str(ptr)
		buckets_standard = self.__init_buckets(s_ptr)

		if len(self.low) < len(self.high):
			s_ptr_low = "9" * len(str(self.low))
			buckets_low = self.__init_buckets(s_ptr_low)
		
		while ptr != low - 1:
			if len(str(ptr)) == len(self.high):
				buckets = buckets_standard
			elif len(str(ptr)) < len(self.high):
				buckets = buckets_low

			for divider, (bucket, slot_size) in buckets.items():
				if len(set(bucket)) == 1:
					self.violations_2.add(ptr)

				if bucket[-1] == 0:
					r_idx = self.__find_nonzero_right_slot(bucket)
					bucket[r_idx] -= 1
					for i in range(r_idx + 1, len(bucket)): 
						bucket[i] = int("9" * slot_size)
					continue

				bucket[-1] -= 1

			ptr -= 1

		return self.violations_2

	def __find_nonzero_right_slot(self, bucket):
		i = 0
		for slot in reversed(bucket):
			if slot != 0:
				break
			i += 1
		return len(bucket) - 1 - i
		
	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return f"{self.low}-{self.high}"

class Database:
	def __init__(self):
		self.filename = "input_day2.txt"
		self.ranges = []
		self.violations_1 = []
		self.violations_2 = []
		self.__parse_file()

	def __parse_file(self):
		ranges = open(self.filename).read().split(",")
		ranges = [ranje.split("-") for ranje in ranges]
		self.ranges = list(map(lambda x: Range(x[0], x[1]), ranges))

	def find_violations_1(self):
		for ranje in self.ranges:
			self.violations_1.extend(ranje.find_violations_1())

	def find_violations_2(self):
		for ranje in self.ranges:
			self.violations_2.extend(ranje.find_violations_2_fast())

	@property
	def invalid_id_sum_1(self):
		return sum(self.violations_1)

	@property
	def invalid_id_sum_2(self):
		return sum(self.violations_2)

if __name__ == "__main__":
	start = time.time()
	db = Database()
	db.find_violations_1()
	print(db.violations_1)
	print(db.invalid_id_sum_1)
	db.find_violations_2()
	print(db.violations_2)
	print(db.invalid_id_sum_2)
	end = time.time()
	print("Execution time:", round(end - start, 3), "s")


'''
	Initial Code

	def find_violations_2_fast(self):
		ptr = int(self.high)
		s_ptr = str(ptr)
		# print("s_ptr", s_ptr, "low", self.low, "high", self.high, "len(self.high)", len(self.high))
		len_ptr = len(self.high)
		dividers = list(filter(lambda x: len_ptr // x == len_ptr / x, list(range(2, len_ptr + 1))))
		buckets = dict()
		# print("\nNew")
		# print(dividers)
		for divider in dividers:
			slot_size = len(s_ptr) // divider
			for i in range(divider):
				new_bucket = int(s_ptr[i*slot_size:(i+1)*slot_size])
				if buckets.get(divider) != None:
					buckets[divider][0].append(new_bucket)
				else:
					buckets[divider] = [[new_bucket], slot_size]


		s_ptr_low = "9" * len(str(self.low))
		dividers_low = list(filter(lambda x: len(self.low) // x == len(self.low) / x, list(range(2, len_ptr + 1))))
		buckets_low = dict()
		# print("\nNew low")
		# print(dividers_low)
		for divider in dividers_low:
			mid = len(s_ptr_low) // divider
			for i in range(divider):
				# print("len(s_ptr)", len(s_ptr), "divider", divider)
				new_bucket = int(s_ptr_low[i*mid:(i+1)*mid])
				if buckets_low.get(divider) != None:
					buckets_low[divider][0].append(new_bucket)
				else:
					buckets_low[divider] = [[new_bucket], mid]
		# print(buckets_low)
		
		low = int(self.low)
		while ptr != low - 1:
			# print("\nptr", ptr)

			#Try normal buckets
			if len(str(ptr)) == len(self.high):
				for divider, (bucket, slot_size) in buckets.items():

					idx = -1
					# print("idx", idx, "bucket", bucket)

					if len(set(bucket)) == 1:
						# print("match", "bucket", bucket, "ptr", ptr, "divider", divider)
						self.violations_2.add(ptr)

					if bucket[idx] == 0:
						#find righ most bucket with non zero
						r_idx = self.__find_nonzero_right_slot(bucket)
						# print(r_idx, "r_idx")
						bucket[r_idx] -= 1
						# print("bucket r_idx", bucket)
						for i in range(r_idx + 1, len(bucket)): 
							bucket[i] = int(str(9) * slot_size)
						# print("bucket", bucket)
						continue

					bucket[idx] -= 1
					# print("bucket", bucket)

			#Try smaller buckets
			elif len(str(ptr)) < len(self.high):
				for divider, (bucket, slot_size) in buckets_low.items():
					idx = -1
					# print("idx", idx, "bucket", bucket)

					if len(set(bucket)) == 1:
						# print("match", bucket, ptr)
						self.violations_2.add(ptr)

					if bucket[idx] == 0:
						#find righ most bucket with non zero
						r_idx = self.__find_nonzero_right_slot(bucket)
						# print(r_idx, "r_idx")
						bucket[r_idx] -= 1
						# print("bucket r_idx", bucket)
						for i in range(r_idx + 1, len(bucket)): 
							bucket[i] = int(str(9) * slot_size)
						# print("bucket", bucket)
						continue

					bucket[idx] -= 1
					# print("bucket", bucket)

			ptr -= 1

		return self.violations_2
'''