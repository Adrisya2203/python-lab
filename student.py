class Student:
    tutorname = "Bindhumiss"  # Class variable (shared by all instances)

    def __init__(self, n, a):
        self.name = n  # Instance variable for name
        self.age = a   # Instance variable for age

    def display(self):
        print(self.name)  # Display student's name
        print(self.age)   # Display student's age
        print(self.__class__.tutorname)  # Access class variable 'tutorname'

    def compare(self, other):
        if self.age == other.age:
            return True  # Return True if ages are the same
        else:
            return False  # Return False if ages are not the same
s1 = Student("Josiya", 21)
s2 = Student("Anita", 21)
s1.display()
print(s1.compare(s2))

