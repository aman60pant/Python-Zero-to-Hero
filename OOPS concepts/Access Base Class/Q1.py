# Create Parent with method display().
# Make Child that overrides display().
# Access parent’s version using: 
# # Parent.display(self)            # super().display()             # super(Child, self).display()

class Parent:
    def display(self):
        print("Mehtod of base class.")

class Derived(Parent):
    def display(self):
        print("Mehtod of derived class.")

        # Method 1: Direct class reference
        Parent.display(self)
        
        # Method 2: super() - recommended
        super().display()
        
        # Method 3: super(ClassName, self)
        super(Derived, self).display()



obj = Derived()
obj.display()