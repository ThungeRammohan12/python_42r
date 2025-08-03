# Practice problem solving on  list comprehension
# Rotate a list by k positions to the right.
# Example:
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
def rotate_right(a,k):
    n = len(a)
    k = k%n
    return a[-k:]+a[:-k]

a = [1, 2, 3, 4, 5]
k = 2           
print(rotate_right(a, k))

# Remove all duplicates from a list without using set().
# Input: [1, 2, 3, 2, 1, 4, 5]
# Output: [1, 2, 3, 4, 5]
def remove_dup(a):
    result = []
    [result.append(i) for i in a if i not in result]
    return result

a = [1, 2, 3, 2, 1, 4, 5]
print(remove_dup(a))

# Find all pairs in a list that sum up to a target.
# Input: lst = [2, 4, 3, 5, 7], target = 7
# Output: [(2, 5), (4, 3)]
def paris(a,target):
    result = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == target:
                result.append((a[i], a[j]))
    return result
a = [2, 4, 3, 5, 7]
target = 7      
print(paris(a, target))

# Flatten a 2D list without using built-in flatten functions.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]
def flatten(a):
    result = [item for sublist in a for item in sublist]
    return result
a = [[1, 2], [3, 4], [5]]
print(flatten(a))

# Count the frequency of each element in a list and return a dictionary.
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}
def count_frequency(a):
    freq= {}
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1 
    return freq
a = [1, 2, 2, 3, 1, 4, 2]
print(count_frequency(a))

# Part B: Strings (5 Questions)
# Check if a string is a palindrome (ignoring spaces and case).
# Input: "A man a plan a canal Panama"
# Output: True
def palindrome(s):
    s= s.replace(" ", "").lower()
    return s == s[::-1]
s = "A man a plan a canal Panama"
print(palindrome(s))

# Find the first non-repeating character in a string.
# Input: "aabbcdeff"
# Output: 'c'
def first_non_repeating(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

s = "aabbcdeff"
print(first_non_repeating(s))

# Remove all vowels from a string.
# Input: "Hello World"
# Output: "Hll Wrld"
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])
s = "Hello World"
print(remove_vowels(s))

# Count the number of words in a string without using .split().
# Input: "Python is great"
# Output: 3
def count_words(a):
    count= 0
    for i in a:
        if i == " ":
            count += 1
    return count + 1
a = "Python is great"
print(count_words(a))

# Find the longest word in a sentence.
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"
def longest_word(s):
    words = s.split()
    longest = words[0]
    for word in words:
        if len(word) >= len(longest):
            longest = word
    return longest
s = "The quick brown fox jumps over the lazy dog"
print(longest_word(s))
