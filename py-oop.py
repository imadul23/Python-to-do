class Car:
    wheel = 4

    # The Constructor method to initialize attributes
    def __init__(self, brand, model, color):
        self.brand = brand      # Instance Attribute
        self.model = model      # Instance Attribute
        self.color = color      # Instance Attribute
        self.is_running = False # Default state Attribute

    # A method to simulate driving
    def start_engine(self):
        self.is_running = True
        print(f"The {self.color} {self.brand} {self.model} engine is now running!")

    # A method to display car information
    def display_info(self):
        print(f"Car Details: {self.brand} {self.model} ({self.color})")

class Truck:
    wheel = 6

    # The Constructor method to initialize attributes
    def __init__(self, brand, model, color):
        self.brand = brand      # Instance Attribute
        self.model = model      # Instance Attribute
        self.color = color      # Instance Attribute
        self.is_running = False # Default state Attribute

    # A method to simulate driving
    def start_engine(self):
        self.is_running = True
        print(f"The {self.color} {self.brand} {self.model} engine is now running!")

    # A method to display car information
    def display_info(self):
        return (f"Truck Details: {self.brand} {self.model} ({self.color})")

car1 = Car('tesla', 'x1', 'black')
car2 = Car('tesla2', 'x1', 'black')
truck1 = Truck('truck 1', 'x1', 'black').display_info()

car1.display_info()
print(truck1)
