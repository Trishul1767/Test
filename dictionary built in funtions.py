#dictionary built in funtions
my_dict = {"name": "Trishul", "age": 19, "city": "New York"}
#1. keys() - returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys())   
#2. values() - returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values())
#3. items() - returns a view object that displays a list of dictionary's key-value tuple pairs.
print(my_dict.items())
#4. get() - returns the value of the specified key. If the key does not exist, it returns None (or a default value if provided).
print(my_dict.get("name"))  # Output: Trishul
print(my_dict.get("country", "USA"))  # Output: USA (default value)
#5. pop() - removes the specified key and returns its value. If the key does not exist, it raises a KeyError (or returns a default value if provided).
print(my_dict.pop("age"))  # Output: 19
print(my_dict)  # Output: {'name': 'Trishul', 'city': 'New York'}
print(my_dict.pop("country", "Key not found"))  # Output: Key not found
#6. update() - updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
my_dict.update({"country": "USA", "profession": "Student"})
print(my_dict)  # Output: {'name': 'Trishul', 'city': 'New York', 'country': 'USA', 'profession': 'Student'}
#7. clear() - removes all items from the dictionary, leaving it empty.
my_dict.clear()
print(my_dict)  # Output: {}
