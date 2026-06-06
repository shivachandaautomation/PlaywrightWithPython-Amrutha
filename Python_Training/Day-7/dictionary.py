# python dictionary.py
# # Dictionary methods in Python are built-in functions that can be used to perform various operations on dictionaries, which are collections of key-value pairs. Here are some common dictionary methods:
# no duplicate keys allowed in dictionary
# duplicates allowed in list
# duplicate values allowed in dictionary

example_dict = {'name': 'Alice', 'age': 30, 'city': 'New York', 'city': 'Los Angeles'}
print(example_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'Los Angeles'}
# one more disctionary example
example_dict = {'names': ['Alice','shiva','amrutha'], 'age': 30, 'city': 'New York', 'city': 'Los Angeles', 'city': 'Chicago'}
print(example_dict)

dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(dict1['name'])  # Output: Alice
print(dict1['age'])   # Output: 30
print(dict1['city'])  # Output: New York
print(dict1.get('name'))  # Output: Alice
print(dict1.get('age'))   # Output: 30 
print(dict1.get('city'))  # Output: New York
print(dict1.get('class'))  # Output: None (since 'class' is not a key in the dictionary)
print(dict1['class'])  # This will raise a KeyError since 'class' is not a key in the dictionary

# dictionary other methods:
# 1. keys(): Returns a view object that displays a list of all the keys in the dictionary.
# 2. values(): Returns a view object that displays a list of all the values in the dictionary.
# 3. items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
# 4. update(): Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.
# 5. pop(): Removes the specified key and returns the corresponding value. Raises a KeyError if the key is not found.
# 6. popitem(): Removes and returns an arbitrary key-value pair from the dictionary. Raises a KeyError if the dictionary is empty.
# 7. clear(): Removes all items from the dictionary.

    # examples for above methods:
dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(dict1.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(dict1.values())  # Output: dict_values(['Alice', 30, 'New York'])
print(dict1.items())   # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
dict2 = {'country': 'USA', 'occupation': 'Engineer'}
dict1.update(dict2)
print(dict1)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
print(dict1.pop('age'))  # Output: 30
print(dict1)  # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
print(dict1.popitem())  # Output: ('occupation', 'Engineer') (or any arbitrary key-value pair since dictionaries are unordered)
print(dict1)  # Output: {'name': 'Alice', 'city': 'New  York', 'country': 'USA'}
