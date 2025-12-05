# Day 1

Comparing lists

### Part 1 
- Simply sort the two integer lists
- Zip the two lists
- Loop over to find the abs difference in ear pair
- Sum over the difference in the list

### Part 2
- For each item in left list find occurrence count in right list

### Focus
`sort, list, append, filter, count, map`

# Day 2 

List properties, strict ordering

### Part 1
- Check each list is strictly increasing or strictly decreasing
- Ensure increase/decrease is lower bounded by 1 and upper bounded by 3
- Duplication can be detected by casting to sets and counting its occurrence in list, better to just compare size of list with set.
- Strictly increasing can be checked in one pass O(n) or by sorting the list (both normal and reverse) and comparing with original which is O(n log n)
- Upper bound of 3 is checked by a single pass over list (starting from index 1) return boolean in a list comprehension and using built-in all method 

### Part 2
- Start with simple case of duplication detection
- If more than 1, simply return unsafe
- if exactly 1 remove that duplicate and call part one's isSafe method
- If zero duplicates, then check for ordering case and upper bound 3 case.
- If either case returns true, then return safe because underneath they call part 1 isSafe method that ensures all three preconditions of safety
- For ordering case, zip report with sorted/reverse sorted array, detect first difference in loop, remove that item from report and call isSafe.
- For upper bound 3 case, do one pass and safe differences
- If there is any difference > 3, call isSafe on both positions separately and or the result

### Optimization
-  Currently in ordering case for part 2, I zip safe decreasing report with sorted version (increasing) so it keeps calling isSafe on each iteration. Need to prevent this case and call isSafe directly
- Also, in cases on difference, I remove first difference then call isSafe. Then repeat same for next difference. I can simply return early in this case, like I do for upper bound 3 case. Currently, it is like dumb brute force. I tried but it is causing 1 edge case.

### Focus
`sort, sorted, sorted(reverse=True), list comprehension, all`

# Day 3 

Pattern matching

### Part 1
- Use regex library to detect patterns like from a mul(num1, num2) from a line
- Extract the numbers from each match multiply them add to final result

### Part 2
- Use `|` operator to match multiple expressions like do() and don't()

### Focus
`re.findall, split, strip`

# Day 4

Simple graph traversal

### Part 1
- Traverse 2D array, left to right, top to bottom
- If current slot is X, try to construct XMAS for right case, down case, right down case, right up case.
- Repeat same for S, to find SAMX i.e. reverse for XMAS and add the results
- Only add the result if it does not go out of bounds

### Part 2
- Repeat the right down and right up case
- Repeat for both word (MAS) and word reversed (SAM)
- In each word match, persist the indices for middle word A
- Then count unique instances of common A's where matches are two or more (in our case it can only be maximum two based on the shape of X-MAS) 

### Focus
`enumerate, list.append`

# Day 5

Partial ordering

### Part 1
- Partial ordering is defined on a pair of numbers
- Run compaction to create a rule dictionary which key's priority is greater than all its values'
- The priority within values is not important and if it exists, it is handled by some order key-value pair in the rule dictionary 
- For each update, find all the relevant rules from the rule dictionary
- For all the relevant rules, ensure they are satisfied
- Satisfaction can be checked by ensuring there is no intersection between values of key in the dictionary and the substring in update after the key's index

### Part 2
- Repeat the loop logic for part 1 except where a rule is violated, I add the logic to fix the update given the rule key and values
- How to fix the update is easier if we move all the relevant values after the key in update than move the key before all the relevant values in update
- The later may seem easy as it involves only moving one key in the update but where to move it is not as trivial i.e. detect first occurrence of any of the values in update then move before
- The former is easy, just place all relevant values in update right after key 

### Focus
`set, set.intersection, set.add list.index, dict.get, dictionary comprehensions`
