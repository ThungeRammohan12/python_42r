s = "PythonProgramming"

# 1. Print the first 6 characters
print("1:", s[:6])

# 2. Print the last 6 characters using negative indexing
print("2:", s[-6:])

# 3. Print characters from index 2 to 9
print("3:", s[2:10])

# 4. Print the entire string in reverse
print("4:", s[::-1])

# 5. Print every second character from the string
print("5:", s[::2])

# 6. Print the string excluding the first and last character
print("6:", s[1:-1])

# 7. Print the substring "Programming" using negative index
print("7:", s[-11:])

# 8. Print the substring "Python" using positive index
print("8:", s[0:6])

# 9. Print the substring "thonPro"
print("9:", s[2:9])

# 10. Print every third character from index 0 to 12
print("10:", s[0:13:3])

# 11. Print characters from index -12 to -5
print("11:", s[-12:-5])

# 12. Reverse only the word "Python"
print("12:", s[5::-1])

# 13. Print the middle 4 characters of the string
mid = len(s) // 2
print("13:", s[mid-2:mid+2])

# 14. Print the second last character
print("14:", s[-2])

# 15. Remove first 3 and last 3 characters
print("15:", s[3:-3])
