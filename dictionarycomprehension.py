# 1. Delete a list of keys from a dictionary
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
for key in keys:
    sample_dict.pop(key, None)
print("After deleting keys:", sample_dict)

# 2. Count the frequency of each character in a given string using a dictionary
text = "hello world"
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Character frequency:", freq)

# 3. Create a dictionary with even and odd numbers
numbers = list(range(10))
result = {
    "even": [num for num in numbers if num % 2 == 0],
    "odd": [num for num in numbers if num % 2 != 0]
}
print("Even and Odd dictionary:", result)

# 4. Difference between dict.get() and direct key access
my_dict = {'a': 1, 'b': 2}
# Direct access (will raise error if key doesn't exist)
# print(my_dict['c'])  # KeyError
print("Using get():", my_dict.get('c'))       # Output: None
print("Using get() with default:", my_dict.get('c', 0))    # Output: 0

# 5. Convert a dictionary to a list of tuples
my_dict = {'a': 1, 'b': 2, 'c': 3}
tuple_list = list(my_dict.items())
print("List of tuples:", tuple_list)

# 6. Store names as keys and their lengths as values
names = ["Alice", "Bob", "Charlie"]
lengths = {name: len(name) for name in names}
print("Name lengths dictionary:", lengths)

# 7. Create a dictionary from 1 to 5 with even/odd labels
result = {num: "even" if num % 2 == 0 else "odd" for num in range(1, 6)}
print("Even/Odd label dictionary:", result)

# 8. Create Reverse Word Dictionary
words = ["cat", "dog", "bat"]
reversed_dict = {word: word[::-1] for word in words}
print("Reversed words dictionary:", reversed_dict)

# 9. Sum all the values in a dictionary
my_dict = {'a': 100, 'b': 200, 'c': 300}
total = sum(my_dict.values())
print("Sum of values:", total)
