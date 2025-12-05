# Day 1

### Part 1
Simply sort the two integer lists
Zip the two lists
Loop over to find the abs difference in ear pair
Sum over the difference in the list

### Part 2
For each item in left list find occurrence count in right list

### Focus
sort, list, append, filter, count, map

# Day 2

### Part 1
Check each list is strictly increasing or strictly decreasing
Ensure increase/decrease is lower bounded by 1 and upper bounded by 3
Duplication can be detected by casting to sets and counting its occurrence in list, better to just compare size of list with set.
Strictly increasing can be checked in one pass O(n) or by sorting the list (both normal and reverse) and comparing with original which is O(n log n)
Upper bound of 3 is checked by a single pass over list (starting from index 1) return boolean in a list comprehension and using built-in all method 

### Part 2
Start with simple case of duplication detection
If more than 1, simply return unsafe
if exactly 1 remove that duplicate and call part one's isSafe method
If zero duplicates, then 

### Focus
sort, sorted, sorted with reverse=True, list comprehension, all 
