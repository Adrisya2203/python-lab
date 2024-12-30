class Car:
    numberofwheels = 4  # Class-level variable (shared by all instances)

    def __init__(self, m, c):
        self.mileage = m  # Instance-level variable
        self.company = c

    def display(self):
        print(self.mileage)
        print(self.company)
        print(self.__class__.numberofwheels)


c = Car(19, "BMW")
c.display()

