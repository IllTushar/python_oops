from Car import CarDetails
from Car import CarParts

if __name__ == '__main__':
    car = CarDetails("Tata", "Safari", 4, 3)
    print(car.print_car())
# print(f"Brand:  {car.brand}")
# print(f"Model:  {car.model}")
#

# Polymorphism example
# car = CarDetails("Tata", "Safari", 4, 3)
# print(car.new_message())
#
# car_parts = CarParts(4, 3)
# print(car_parts.new_message())
