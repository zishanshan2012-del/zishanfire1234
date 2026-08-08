class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Create an object
car = Vehicle(240, 18)

# Print the values
print("Maximum Speed:", car.max_speed)
print("Mileage:", car.mileage)