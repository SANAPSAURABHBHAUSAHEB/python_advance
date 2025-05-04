

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def hello(self):
        pass

class Cat(Animal):
    def hello(self):
        print("Hello World !!!")

# a = Animal()
# print(a)

c = Cat()
c.hello()
# print(c.hello())