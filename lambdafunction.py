#  Calculate the sum of digits of a number using a while loop.
# e.g., 123 → 6
n = int(input("Enter a number: "))
sum =0
i=0
while i<=n:
    sum +=i
    i+=1
print(sum)

# Reverse a number using a while loop.
# e.g., 123 → 321
a = int(input("Enter a 3 digit number: "))
reverse = 0

while a > 0:
    digit = a % 10        
    reverse = reverse * 10 + digit  
    a = a // 10           

print("Reversed number:", reverse)

# Intermediate Level
# Check if a number is a palindrome using a while loop.
# e.g., 121 → Palindrome
b = int(input("enter a number to check Palindrome: "))
original = b
palindrome = 0

while b>0:
    digit = b%10
    palindrome = palindrome * 10 + digit
    b = b//10
    
print("Palindrome"if original == palindrome  else "Not palindrome")
