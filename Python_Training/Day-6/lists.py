numbers = [3, 2, 0, 4, 5]
# print(numbers[0])  # Output: 3
# print(numbers[2])  # Output: 0
# print(numbers[-1]) # Output: 5
# # List slicing
# print(numbers[1:4]) # Output: [2, 0, 4]
# print(numbers[:3]) # Output: [3, 2, 0]
# print(numbers[2:]) # Output: [0, 4, 5]
# # List methods
# numbers.append(6)   
# print(numbers)  # Output: [3, 2, 0, 4, 5, 6]
# numbers.insert(1, 5)
# print(numbers)  # Output: [3, 5, 2, 0, 4, 5, 6]
# numbers.remove(5)
# print(numbers)  # Output: [3, 2, 0, 4, 5, 6]
# numbers.pop()
# print(numbers)  # Output: [3, 2, 0, 4, 5]
# numbers.sort()
# print(numbers)  # Output: [0, 2, 3, 4, 5]
# numbers.reverse()
# print(numbers)  # Output: [5, 4, 3, 2, 0]

# The sorted() function in Python is a built-in function used to sort the elements of an iterable (such as a list, tuple, or string)
# and returns a new sorted list, leaving the original iterable unchanged.

# sorted(iterable, key=None, reverse=False)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)
print(numbers)  # Original list remains unchanged

set1 = {1, 2, 2, 3, 4, 5}
print(set1)  # Output: {1, 2, 3, 4, 5}

list1 = [1, 2, 2, 3, 4, 5]
print(list1)  # Output: [1, 2, 2, 3, 4, 5]
set2 = set(list1)
print(set2)  # Output: {1, 2, 3, 4, 5}
l2 = list(set2)
print(l2)  # Output: [1, 2, 3, 4, 5]

list5 = [1,2,3,4,4,5,6,6,7,7, ]
unique_numbers = list(set(list5))
print(unique_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7]

# List methods in Python are built-in functions that can be used to perform various operations on lists, which are ordered collections of items. Here are some common list methods:
# 1. append(): Adds an item to the end of the list.   
# 2. insert(): Inserts an item at a specified position in the list.
# 3. remove(): Removes the first occurrence of a specified item from the list.
# 4. pop(): Removes and returns the item at a specified position in the list. If no index is specified, it removes and returns the last item.
# 5. sort(): Sorts the items of the list in place (i.e., it modifies the original list).
# 6. reverse(): Reverses the order of the items in the list in place.
# 7. clear(): Removes all items from the list.

