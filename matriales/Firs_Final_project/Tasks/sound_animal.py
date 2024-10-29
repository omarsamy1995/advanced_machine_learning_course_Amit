from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing a general animal."""
    
    @abstractmethod
    def make_sound(self):
        """Abstract method to be implemented by subclasses to return the animal's sound."""
        pass

    def describe(self):
        """Concrete method to describe general animal characteristics."""
        print("This is an animal with unique characteristics.")

class Dog(Animal):
    """Derived class representing a Dog."""
    
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    """Derived class representing a Cat."""
    
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    """Derived class representing a Cow."""
    
    def make_sound(self):
        return "Moo!"

def create_animal(animal_type):
    """Factory function to create an animal instance based on user input."""
    animal_classes = {
        'dog': Dog,
        'cat': Cat,
        'cow': Cow
    }
    animal_class = animal_classes.get(animal_type.lower())
    if animal_class:
        return animal_class()
    else:
        print("Invalid animal type. Please enter 'dog', 'cat', or 'cow'.")
        return None

# Main program to get user input and create animal
def main():
    animal_type = input("Enter the type of animal (dog, cat, cow): ").strip()
    animal = create_animal(animal_type)
    
    if animal:
        animal.describe()
        print(f"The animal makes this sound: {animal.make_sound()}")

if __name__ == "__main__":
    main()