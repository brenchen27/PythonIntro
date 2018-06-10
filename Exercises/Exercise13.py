class Animal:

    def __init__(self, **kwargs):
        self.name=kwargs["name"]
        self.weight=kwargs["weight"]
        self.sound=kwargs["sound"]

    def __str__(self):
        return f"{self.name} is an animal"

cat = Animal(name="cat",weight="10",sound="meow")
dog = Animal(name="dog",weight="20",sound="bark")

class Cat(Animal):

    def __init__(self, **kwargs):
        self.breed=kwargs["breed"]
        super().__init__(**kwargs)

    def __str__(self):
        return f"{self.name} is a {self.breed} cat"

cat1=Cat(name="tom", weight="7", sound="meow", breed="Persian")
cat2=Cat(name="jerry 2", weight="3", sound="meow", breed="Russian Blue")
cat3=Animal(name="jerry 3", weight="3", sound="meow", breed="Persian")

print(cat2)
print(cat3)

class Dog(Animal):

    def __init__(self, **kwargs):
        self.breed=kwargs["breed"]
        super().__init__(**kwargs)

    def __str__(self):
        return f"{self.name} is a {self.breed} dog"

dog1=Dog(name="fat", weight="57", sound="woof", breed="golden retriever")
dog2=Dog(name="more fat", weight="57432890", sound="grunt", breed="black lab")
dog3=Dog(name="skinny", weight="0.0003", sound="woof", breed="shitzu")

print(dog3)
