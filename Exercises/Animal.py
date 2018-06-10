class Animal:

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def compareWeight(self, anotherAnimal):
        if self.weight > anotherAnimal.weight:
            print(self.name + " weight is greater than " + anotherAnimal.name)
        elif self.weight < anotherAnimal.weight:
            print(self.name + " weight is less than " + anotherAnimal.name)
        else:
            print(self.name + " weight is the same as " + anotherAnimal.name)

animal1 = Animal("dog","white","11")
animal2 = Animal("cat","white","9")

animal1.compareWeight(animal2)
