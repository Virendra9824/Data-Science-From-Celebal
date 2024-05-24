class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
    
    def fare(self):
        standard_fare = super().fare()
        maintenance_charge = 0.10 * standard_fare
        total_fare = standard_fare + maintenance_charge
        return total_fare


bus = Bus(seating_capacity=20)
print(f"Total fare for the bus is Rs {bus.fare()}")
