# #### 🔁 *Questions Involving Loops*

# 1. Write a program to print the sum of all even numbers between 1 and 100.
def sum_even():
    count = 0
    for i in range(1,101):
        if i%2==0:
          count+=i
    return count
print(sum_even())

# 2. Write a program that prints the first 10 powers of 2 using a loop.
def power():
   for i in range(0,11):
       print(2**i)

power()
        
# 3. Calculate the factorial of a number entered by the user.
def fact(a):
   fac = 1
   for i in range(1,a+1):
        fac *= i
   return fac

print(fact(6))

# 4. Print the reverse of a given number (e.g., input 1234 → output 4321).
def rev_num(a):
    rev = 0
    while a>0:
        digit = a%10
        rev = rev*10 + digit
        a= a//10
    return rev
print(rev_num(1234))

# 5. Count the number of digits in a given integer using a loop.
def count_digit (a):
    count = 0
    while a>0:
        a = a//10
        count +=1
    return count
print(count_digit(5688589))
# 6. Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5.
def div():
    for i  in range(1,101):
        if i%3 == 0 and i%5 == 0:
            print(i)
div()
# 7. Without using multiplication, calculate a * b using addition and a loop.
def Mul(a,b):
    result = 0
    for i in range(b):
        result +=a
    return result
print(Mul(5,3))
# 8. Print the sum of digits of a number entered by the user (e.g., 123 → 1+2+3 = 6).
def sum_digit(a):
    sum = 0
    while a>0:
        b= a%10
        sum +=b
        a = a//10
    return sum
print(sum_digit(1234))

# 9. Write a loop to check if a number is a palindrome (number reads the same forwards and backwards).
def pal(a):
    original = a
    rev = 0
    while a>0:
        digit = a%10
        rev = rev*10 + digit
        a = a//10
    if original == rev:
        return "palin"
    else:
        return "not palin"
    
print(pal(12321))
    
# 10. Write a program to find the highest digit in a given number.
def high_digit(a):
    highest = 0
    while a>0:
        digit = a%10
        if digit >highest:
            highest = digit
        a = a//10
    return highest
    
print(high_digit(12465))

# #### 🔀 *Questions Involving Conditionals*

# 11. Write a program to check if a number is positive, negative, or zero.
def check_num(a):
    if a>0:
        return "Positive"
    elif a<0:
        return "Negative"
    else:
        return "Zero"

print(check_num(-5))
# 12. Write a program that takes a number and prints whether it is divisible by 2, 3, both, or neither.
def div_2_3(a):
    if a%2 == 0 and a%3 ==0:
        return "Divisible by both 2 and 3"
    elif a %2 ==0:
        return "Divisible by 2"
    elif a%3 ==0:
        return "Divisible by 3"
    else:
        return "Not divisible by 2 or 3"
print(div_2_3(6))

# 13. Check if a number is a three-digit number using conditionals.
def check_3_digit(a):
    if 100<=a<=999:
        return "Three_digit number"
    else:
        return "Not a three-digit number"
print(check_3_digit(123))

# 14. Write a program to check whether a given number is a prime number.
def prime(a):
    is_prime = True
    if a<2:
        is_prime = False
    else:
        for i in range(2, int(a**0.5)+1):
            if a%i ==0:
                is_prime = False
                break
            else:
                is_prime = True
                break
    if is_prime:
        return f"{a} is  a prime number"
    else:
        return f"{a} is not a prime number"
    
print(prime(29))

# 15. Write a program to find the largest of three numbers entered by the user using nested if-else.
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return f"{a} is the largest number"
    elif b >= a and b >= c:
        return f"{b} is the largest number"
    else:
        return f"{c} is the largest number"
print(largest_of_three(10, 20, 15))
# 16. Check if a year is a leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
print(is_leap_year(2020))

# 17. Take an integer input and determine if it is even and greater than 50.
def even_greater_than_50(a):
    if a % 2 == 0 and a > 50:
        return f"{a} is even and greater than 50"
    else:
        return f"{a} is not even or not greater than 50"
print(even_greater_than_50(60))

# 18. Write a program to classify a number as:
# * Less than 0: "Negative"
# * 0 to 9: "Single Digit"
# * 10 to 99: "Two Digits"
# * 100 and above: "Three or More Digits"
def classify_number(a):
    if a < 0:
        return "Negative"
    elif 0 <= a <= 9:
        return "Single Digit"
    elif 10 <= a <= 99:
        return "Two Digits"
    else:
        return "Three or More Digits"
print(classify_number(45))

# 19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square.
def square_greater_than_1000(a):
    square = a ** 2
    if square > 1000:
        return f"The square of {a} is {square}, which is greater than 1000"
    else:
        return f"The square of {a} is {square}, which is not greater than 1000"
    
print(square_greater_than_1000(35))

# 20. Take two integers as input and determine if one is a factor of the other.
def is_factor(a, b):
    if a % b == 0:
        return f"{b} is a factor of {a}"
    elif b % a == 0:
        return f"{a} is a factor of {b}"
    else:
        return f"Neither {a} nor {b} is a factor of the other"
print(is_factor(10, 5))
