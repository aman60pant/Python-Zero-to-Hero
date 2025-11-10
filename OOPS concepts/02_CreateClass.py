# Create a class Car with attributes brand, model, and year. Write a method display_info() to print the car’s details.

class Car:
    brand = "BMW"
    model = "m5"
    year = 2025

    def display_info():
        print(f"You have an {Car.brand} of model {Car.model} made in year {Car.year}")

new_car = Car()
Car.display_info()