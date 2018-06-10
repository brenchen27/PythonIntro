class Movies:

    ratings={"g":"kids","pg13":"teenage","r":"adult"}

    def __init__(self, **kwargs):
        self.title = kwargs["title"]
        self.year = kwargs["year"]
        self.genre = kwargs["genre"]
        self.rating = kwargs["rating"]

    def goodForKids(self):
        if self.rating == "pg":
            outcome="The movie " + self.title + "is good for kids"
        elif self.rating == "pg13":
            outcome="The movie " + self.title + "is not good for kids"
        return outcome

    def __str__(self):
        return "The movie " + self.title + " is a " + self.ratings[self.rating] + " movie"


movies1=Movies(title="back to the future", year="1985", genre="scifi", rating="pg13")
movies2=Movies(title="doctor strange", year="2016", genre="fantasy", rating="pg13")
movies3=Movies(title="shrek", year="2001", genre="fantasy", rating="pg")

print(movies1)
