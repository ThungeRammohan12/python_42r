# 1. Invert a dictionary with list values (group keys by their values)
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
inverted = {}
for key, value in d.items():
    inverted.setdefault(value, []).append(key)
print("Inverted Dictionary:", inverted)

# 2. Find Max and Min Value in Dictionary
d = {'a': 10, 'b': 5, 'c': 15}
print("Max Value:", max(d.values()))
print("Min Value:", min(d.values()))

# 3. Dictionary comprehension for prime check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = [2, 3, 4, 5, 6]
prime_dict = {num: "prime" if is_prime(num) else "notprime" for num in nums}
print("Prime Check Dictionary:", prime_dict)

# 4. Explain setdefault function
print("setdefault() explanation:")
print("Used to insert a key with a default value if it is not already in the dictionary.")
print("Example:")
d = {}
d.setdefault('a', []).append(1)
print(d)  # {'a': [1]}

# 5. Difference between d[key] and d.get(key)
print("Difference between d[key] and d.get(key):")
print("d[key] raises KeyError if key not found.")
print("d.get(key) returns None or default if key not found.")
example_dict = {'a': 1}
print(example_dict.get('b'))  # Output: None
# print(example_dict['b'])  # Uncommenting this would raise KeyError

# 6. Shallow Copy vs Deep Copy
import copy
original = {'a': [1, 2], 'b': [3, 4]}
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original['a'].append(99)
print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

# 7. Count Vowels in String with Dict Comprehension
s = "welcome to python programming"
vowels = "aeiou"
vowel_count = {ch: s.count(ch) for ch in vowels if ch in s}
print("Vowel Count:", vowel_count)

# 8. Automorphic Number
def is_automorphic(n):
    return str(n * n).endswith(str(n))

nums = [5, 6, 76, 25]
for num in nums:
    print(f"{num} is Automorphic? {'Yes' if is_automorphic(num) else 'No'}")
