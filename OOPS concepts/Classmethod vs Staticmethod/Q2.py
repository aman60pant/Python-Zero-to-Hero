# Create Laptop class with @classmethod from_string(cls, spec)
# spec = "Dell-16GB-512GB" → should create object with these attributes.

class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    @classmethod
    def from_string(cls, spec):
        brand, ram, storage = spec.split("-")
        return cls(brand, ram, storage)


lap = Laptop.from_string("Dell-16GB-512GB")

print(lap.brand)
print(lap.ram)
print(lap.storage)