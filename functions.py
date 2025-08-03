# 1. Function without arguments
def greet():
    print("Hello! Welcome to Python Functions")

greet()
print()

# 2. Function with arguments
def add(a, b):
    print("Sum:", a + b)

add(5, 3)
print()

# 3. Function with return value
def square(n):
    return n * n

result = square(4)
print("Square:", result)
print()

# 4. Function with default arguments
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Alice")
print()

# 5. Function with loop
def print_table(n):
    print(f"Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print_table(5)
print()

# 6. Function using if-else
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print("Is 6 even?", is_even(6))
print("Is 7 even?", is_even(7))
print()

# 7. Function with list argument
def print_list_items(items):
    print("List items:")
    for item in items:
        print("-", item)

print_list_items(["apple", "banana", "cherry"])
print()

# 8. Function with multiple return values
def calc(a, b):
    return a + b, a - b, a * b, a / b

sum_, diff, prod, div = calc(10, 2)
print("Sum:", sum_, "Difference:", diff, "Product:", prod, "Division:", div)
