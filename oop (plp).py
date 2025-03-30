class Vehicle:
    """Base class representing a generic vehicle"""
    
    def __init__(self, make, model, year, color):
        """Constructor to initialize vehicle attributes"""
        self._make = make  # Encapsulated with underscore
        self._model = model
        self._year = year
        self._color = color
        self._mileage = 0  # Default mileage
        self._fuel_level = 100  # Percentage
    
    # Getter methods (encapsulation)
    def get_make(self):
        return self._make
    
    def get_model(self):
        return self._model
    
    def get_year(self):
        return self._year
    
    def get_color(self):
        return self._color
    
    def get_mileage(self):
        return self._mileage
    
    def get_fuel_level(self):
        return self._fuel_level
    
    # Methods to modify vehicle state
    def drive(self, distance):
        """Simulate driving the vehicle"""
        if self._fuel_level <= 0:
            print("Out of fuel! Cannot drive.")
            return
        
        fuel_used = distance * 0.05  # Assume 0.05% fuel per unit distance
        self._fuel_level = max(0, self._fuel_level - fuel_used)
        self._mileage += distance
        print(f"Drove {distance} units. Current mileage: {self._mileage}")
    
    def refuel(self, amount):
        """Add fuel to the vehicle"""
        self._fuel_level = min(100, self._fuel_level + amount)
        print(f"Added {amount}% fuel. Current fuel level: {self._fuel_level}%")
    
    def repaint(self, new_color):
        """Change the vehicle's color"""
        self._color = new_color
        print(f"Vehicle repainted to {new_color}")
    
    def __str__(self):
        """String representation of the vehicle"""
        return (f"{self._year} {self._make} {self._model} "
                f"(Color: {self._color}, Mileage: {self._mileage}, "
                f"Fuel: {self._fuel_level}%)")

class ElectricVehicle(Vehicle):
    """Subclass representing electric vehicles (demonstrates inheritance)"""
    
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)
        self._battery_capacity = battery_capacity  # in kWh
        self._charge_level = 100  # Percentage
    
    # Polymorphism - override drive method
    def drive(self, distance):
        if self._charge_level <= 0:
            print("Battery depleted! Cannot drive.")
            return
        
        charge_used = distance * 0.2  # Assume 0.2% charge per unit distance
        self._charge_level = max(0, self._charge_level - charge_used)
        self._mileage += distance
        print(f"Drove {distance} units electrically. Current mileage: {self._mileage}")
    
    def charge(self, amount):
        """Charge the battery"""
        self._charge_level = min(100, self._charge_level + amount)
        print(f"Charged {amount}%. Current charge: {self._charge_level}%")
    
    def get_battery_capacity(self):
        return self._battery_capacity
    
    def get_charge_level(self):
        return self._charge_level
    
    def __str__(self):
        """String representation with electric-specific info"""
        return (f"{super().__str__()}, "
                f"Battery: {self._battery_capacity}kWh, "
                f"Charge: {self._charge_level}%")

# Demonstration
if __name__ == "__main__":
    print("=== Vehicle Class Demonstration ===")
    
    # Create a regular vehicle
    my_car = Vehicle("Toyota", "Camry", 2022, "Blue")
    print("\nRegular Vehicle:")
    print(my_car)
    
    # Demonstrate methods
    my_car.drive(50)
    my_car.drive(30)
    my_car.refuel(20)
    my_car.repaint("Red")
    print(my_car)
    
    # Create an electric vehicle
    my_ev = ElectricVehicle("Tesla", "Model 3", 2023, "White", 75)
    print("\nElectric Vehicle:")
    print(my_ev)
    
    # Demonstrate polymorphic behavior
    my_ev.drive(40)
    my_ev.drive(60)
    my_ev.charge(30)
    print(my_ev)