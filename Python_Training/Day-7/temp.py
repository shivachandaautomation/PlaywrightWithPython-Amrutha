# example_set = {1, 2, 3}
# print(example_set.pop())
# example_set.remove

# example_dict = {'name': 'Alice', 'age': 30, 'city': 'New York', 'city': 'Los Angeles', 'city': 'Chicago'}
# print(example_dict)

# dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(dict1['name'])  # Output: Alice 
# print(dict1.get('class'))  # Output: None (since 'class' is not a key in the dictionary)
# print(dict1['class'])  # This will raise a KeyError since 'class' is not a key in the dictionary

# dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(dict1.keys())   # Output: <class 'dict_keys'>
# print(dict1.values())  # Output: dict_values(['Alice', 30, 'New York'])
# print(dict1.items())   # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
# dict2 = {'country': 'USA', 'occupation': 'Engineer'}    
# dict1.update(dict2)
# print(dict1)  # Output: {'name': 'Alice', 'age': 30
# # , 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
# print(dict1.pop('age'))  # Output: 30
# print(dict1)  # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
# print(dict1.popitem())  # Output: ('occupation', 'Engineer') (or any
# # arbitrary key-value pair since dictionaries are unordered)
# print(dict1)  # Output: {'name': 'Alice', 'city': 'New

# dict2 = {'name': 'apple', 'occupation': 'Engineer'}
# dict1.update(dict2)
# print(dict1)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}

dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(dict1.keys())    # Output: dict_keys(['name', 'age', 'city'])
# print(dict1.values())  # Output: dict_values(['Alice', 30, 'New York'])
# print(dict1.items())   # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
dict2 = {'country': 'USA', 'occupation': 'Engineer'}
dict1.update(dict2)
print(dict1)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
print(dict1.pop('age'))  # Output: 30
print(dict1)  # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}
print(dict1.popitem())  # Output: ('occupation', 'Engineer') (or any arbitrary key-value pair since dictionaries are unordered)
print(dict1)  # Output: {'name': 'Alice', 'city': 'New