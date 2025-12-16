from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        return "Roar"

class Tiger(Animal):
    def sound(self):
        return "Growl"

lion = Lion()
tiger = Tiger()

print(f"Lion: {lion.sound()}")
print(f"Tiger: {tiger.sound()}")
