# Base Class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method.")

# Subclass: Dog
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Subclass: Bird
class Bird(Animal):
    def move(self):
        print("Flying 🐦")

# Subclass: Fish
class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

# Subclass: Snake
class Snake(Animal):
    def move(self):
        print("Slithering 🐍")

# Subclass: Kangaroo
class Kangaroo(Animal):
    def move(self):
        print("Hopping 🦘")

# Function to demonstrate polymorphism
def animal_moves(animal: Animal):
    animal.move()

# Test the polymorphic behavior
if __name__ == "__main__":
    animals = [Dog(), Bird(), Fish(), Snake(), Kangaroo()]

    for a in animals:
        animal_moves(a)
