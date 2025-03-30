class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """This will be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement move()")
    
    def __str__(self):
        return self.name

class Car(Vehicle):
    """Car vehicle type"""
    def move(self):
        return f"{self.name} is driving on the road"
    
    def honk(self):
        return "Honk honk!"

class Airplane(Vehicle):
    """Airplane vehicle type"""
    def move(self):
        return f"{self.name} is flying through the air"
    
    def take_off(self):
        return "Taking off on the runway!"

class Boat(Vehicle):
    """Boat vehicle type"""
    def move(self):
        return f"{self.name} is sailing on the water"
    
    def anchor(self):
        return "Dropping anchor!"

class Bicycle(Vehicle):
    """Bicycle vehicle type"""
    def move(self):
        return f"{self.name} is being pedaled on the path"
    
    def ring_bell(self):
        return "Ring ring!"

def demonstrate_movement(vehicles):
    """Demonstrate polymorphism by calling move() on different vehicle types"""
    print("\n=== Movement Demonstration ===")
    for vehicle in vehicles:
        print(vehicle.move())
        # Demonstrate unique methods for each type
        if isinstance(vehicle, Car):
            print(vehicle.honk())
        elif isinstance(vehicle, Airplane):
            print(vehicle.take_off())
        elif isinstance(vehicle, Boat):
            print(vehicle.anchor())
        elif isinstance(vehicle, Bicycle):
            print(vehicle.ring_bell())
        print()  # Blank line for spacing

if __name__ == "__main__":
    # Create a list of different vehicles
    vehicles = [
        Car("Toyota Camry"),
        Airplane("Boeing 747"),
        Boat("Sailfish"),
        Bicycle("Mountain Bike")
    ]
    
    # Demonstrate polymorphism
    demonstrate_movement(vehicles)
    
    # Additional demonstration of the same interface
    print("\n=== Individual Movement Examples ===")
    car = Car("Honda Civic")
    plane = Airplane("Airbus A380")
    
    print(car.move())  # Outputs driving behavior
    print(plane.move())  # Outputs flying behavior