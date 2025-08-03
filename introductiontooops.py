# 1. Student Class
class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade

# 2. Car Class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed = max(0, self.speed - 10)

    def status(self):
        print(f"{self.brand} {self.model} ({self.year}) is going {self.speed} km/h")

# 3. Book Class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def is_long(self):
        return self.pages > 300

# 4. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# 5. BankAccount Class
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"{self.holder}'s balance: ₹{self.balance}")
