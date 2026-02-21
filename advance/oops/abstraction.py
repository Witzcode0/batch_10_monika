from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self, voice_type):
        pass

class Cat(Animal):
    def speak(self, voice_type):
        print(voice_type)

class Dog(Animal):
    def speak(self, voice_type):
        print(voice_type)


c = Cat()
c.speak("Meow meow")

d = Dog()
c.speak("Bhow Bhow")