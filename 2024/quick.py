# Filter dict based on keys
relevant_rules = {key: value for key, value in y.rules.items() if key in update}

# Add or update list in dict
if self.dict.get(key) != None:
	self.dict[key] = [value]
else:
	self.dict[key].append(value)

# Add or update list in dict (one liner)
self.rules[key] = self.rules[key]+[val] if self.rules.get(key) != None else [val]

# 
