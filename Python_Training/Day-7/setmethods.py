# set methods in Python are used to perform various operations on sets, which are unordered collections of unique elements.
# Here are some common set methods:
# 1. add(): Adds an element to the set.
# 2. remove(): Removes a specified element from the set. Raises a KeyError if the element is not found.
# 3. discard(): Removes a specified element from the set if it is present. Does not raise an error if the element is not found.
# 4. pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
example_set = {1, 2, 3}
example_set.add(4)
print(example_set)  # Output: {1, 2, 3, 4}
example_set.remove(2)
print(example_set)  # Output: {1, 3, 4}
example_set.remove(5)  # This will raise a KeyError since 5 is not in the set
example_set.discard(3)  
print(example_set)  # Output: {1, 4}
example_set.discard(5)  # This will not raise an error since discard does not raise an error if the element is not found        
print(example_set.pop())  # Output: 1 (or 4, since sets are unordered)
# 5. clear(): Removes all elements from the set.
example_set.clear()
print(example_set)  # Output: set() 

