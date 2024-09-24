class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = None
        self.__gender = gender
        self.set_age(age)  # Validate age via setter
    
    # Getter for name
    def get_name(self):
        return self.__name
    
    # Setter for name (if needed)
    def set_name(self, name):
        self.__name = name
    
    # Getter for age
    def get_age(self):
        return self.__age
    
    # Setter for age with validation
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer.")
    
    # Getter for gender
    def get_gender(self):
        return self.__gender
    
    # Setter for gender (if needed)
    def set_gender(self, gender):
        self.__gender = gender
    
    # Method to introduce the person with a customizable greeting
    def introduce(self, greeting="Hello"):
        print(f"{greeting}, my name is {self.__name}. I am {self.__age} years old and my gender is {self.__gender}.")
    
# Creating an instance of the Person class
person1 = Person("John Doe", 30, "Male")

# Calling the introduce method
person1.introduce("Hi there")
