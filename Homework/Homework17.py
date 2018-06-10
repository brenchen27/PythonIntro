class Videogames:

    def __init__(self, game, rating, console):
        self.game=game
        self.rating=rating
        self.console=console

    def familyFriendly(self):
        if self.rating=="e":
            print("True")
        elif self.rating=="e 10+":
            print("True")
        elif self.raating=="t":
            print("True")
        else:
            print("False")

videogames1=Videogames("wii sports", "e", "wii")
videogames2=Videogames("fortnite", "t", "xbox")

videogames1.familyFriendly()
