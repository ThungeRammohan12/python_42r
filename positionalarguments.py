# 1. Write a function that prints "Hello, World!".
def welcome():
    print("Hello, World!")

welcome()
# 2. Write a function that takes a name as a parameter and prints a welcome message.
def greeting(name):
    print("Welcome to my world", name)
    
greeting ("Prem")
# 3. Create a function that takes two numbers as parameters and prints their sum.
def add(a,b):
    print(a+b)

add(5,6)
# 4. Write a function that returns the square of a number
def square(n):
    return n*n
    
print(square(2))
# 5. Define a function that multiplies three numbers and returns the result.
def mul(a,b,c):
    return a*b*c
    
print(mul(12,6,7))

# 6. Create a function that checks if a number is even or odd and returns "Even" or "Odd".
def even_num(n):
    if n%2 ==0:
        print("Even")
    else:
        print("Odd")

even_num(36)
# 7. Write a function that takes a number and returns True if it's prime, otherwise False.
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
    
print(prime(13))
# 8. Create a function that returns the factorial of a number.
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(fact(6))  

# 9. Write a function that takes a list of numbers and returns their average.

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

num = [1,2,3,4,5]
print(average(num))

# 10. Create a function that finds the largest of three given numbers.
def largest(a,b,c):
    return max(a,b,c)
    
print(largest(12,55,6))

# 11. Write a function that takes a name and age, and prints them. If age is not given, default to 18.
def employee(name, age=18):
    print("Your name is ",name, "and your age is" ,age)
    
employee("Prem")
# 12. Create a function to calculate simple interest. Default the rate to 5% if not provided.
def interest(p,t, r=5):
    simple_interest = (p*t*r)/100
    return simple_interest

print(interest(1000,2,7))
# 13. Define a function that takes a string and a number. It should print the string that many times. If number is not given, default to 1.
def name(string, num=1):
    for i in range(num):
        print(string)

name("Prem", 13)
# 14. Write a function that takes a list and returns a new list with only the even numbers.
def even_list(a):
    even =[]
    for i in a:
        if i%2 ==0:
            even.append(i)
    return even

num = [1,2,4,5,6,7]
print(even_list(num))
# 15. Create a function that takes a sentence and returns the number of words.
def sentence_count(a):
    a = a.split()
    return len(a)

b = "This is a good place"
print(sentence_count(b))
# 16. Write a function that counts the number of vowels in a string.
def vowels(a):
    count = 0
    for i in a:
        if i=="a" or i =="e" or i=="i" or i=="o" or i=="u":
            count+=1
    return count

b = "Education"
print(vowels(b))
# 17. Write a function that returns the Fibonacci series up to n terms.
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
fib(5)

# 18. Create a function that checks if a string is a palindrome.
def is_palindrome(s):
    s = s.lower() 
    return s == s[::-1] 

print(is_palindrome("Racecar"))  
# 19. Write a function that takes a list of numbers and returns the second largest number.
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None
# 20. Define a function that accepts any number of arguments and returns their sum (use *args).
def sum_of_args(*args):
    return sum(args)
