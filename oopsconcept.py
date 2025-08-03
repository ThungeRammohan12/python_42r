# Define the Person class
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def update_info(self, new_name=None, new_age=None, new_city=None):
        if new_name:
            self.name = new_name
        if new_age:
            self.age = new_age
        if new_city:
            self.city = new_city

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

# Create 5 Person objects
person1 = Person("Alice", 25, "Mumbai")
person2 = Person("Bob", 30, "Delhi")
person3 = Person("Charlie", 22, "Bangalore")
person4 = Person("Daisy", 28, "Hyderabad")
person5 = Person("Ethan", 35, "Chennai")

# Modify each object using update_info()
person1.update_info(new_city="Pune")
person2.update_info(new_age=31)
person3.update_info(new_name="Chuck", new_city="Kolkata")
person4.update_info(new_name="Diana", new_age=29)
person5.update_info(new_name="Eshwar", new_city="Coimbatore")

# Display updated details
person1.display()
person2.display()
person3.display()
person4.display()
person5.display()
