# This is an OOP exercise with an emphasis on the concept of inheritance
# I created two vehicle objects(Car & Truck) and the parent class (Vehicle)
# The Car & Truck objects will inherit the parent Vehicle class's values

class Vehicle:  # The parent class
    def __init__(self, purpose, industry):  # Initialize the Vehicle object
        self.purpose = purpose
        self.industry = industry
    def go(self):  # First method describing the object's purpose
        return self.purpose

    def work(self):  # Second method describing what industry the object belongs to
        return self.industry



class Car(Vehicle):  # Car object and its values inherited from the
                     # Vehicle parent using the super() function
    def __init__(self, purpose, industry):
        super().__init__(purpose, industry)

    def brand(self):  # A method exclusive to the Car object (describes a car brand)
        return 'Toyota'



class Truck(Vehicle):  # Truck object and its values inherited from the
                       # Vehicle parent using the super() function
    def __init__(self, purpose, industry):
        super().__init__(purpose, industry)

    def brand(self): # A method exclusive to the Truck object (describes a truck brand)
        return 'Hino'


# Give the parent class its attributes
v = Vehicle('drive', 'transportation')
print(v.go())  # Calls the go function and prints it which will print the object's purpose (to drive)


# Give the Car object its attributes which it inherits from the parent Vehicle class's values
c = Car('drive', 'transportation')
# Call the functions and print them
print(c.brand())  # Prints the brand function which lists the object's brand (Toyota)
print(c.go())  # Prints the go function which describes the object's purpose (to drive)
print(c.work())  # Prints the work function which describes the object's industry (transportation)


# Give the Truck object its attributes which it inherits from the parent Vehicle class's values
t = Truck('drive', 'transportation')
# Call the functions and print them
print(t.brand()) # Prints the brand function which lists the object's brand (Hino)
print(t.go())  # Prints the go function which describes the object's purpose (to drive)
print(t.work())  # Prints the work function which describes the object's industry (transportation)


# One final print test using the Car object's own brand method and
# its inherited attributes from the Vehicle parent class
print('\nMy favorite form of ' + c.work() + ' is using my brand new ' + c.brand() + ' to ' + c.go() + ' anywhere I want.')


# One final print test using the Truck object's own brand method and
# its inherited attributes from the Vehicle parent class
print('\nAll the ' + t.brand() + ' trucks on the road will ' + t.go() + ' anywhere in the country to serve the ' + t.work() + ' industry.')
