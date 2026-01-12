class Vehicle:
    def general_usage(self):
        print("General usage is: transportation")


class Car(Vehicle):
    def __init__(self):
        print("Car is created")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.specific_usage()
        print("Specific usage is: commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("MotorCycle is created")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.specific_usage()
        print("Specific usage is: road trip, racing")


c = Car()
m = MotorCycle()

print(issubclass(Car, Vehicle))
print(isinstance(Car, MotorCycle))




# Benefits of Inheritance
# 1) Code Reuse
# 2) Extensibility
# 3) Readability