def getZodiac(year):
    a=year-1899
    if year>12:
        if a%12==1:
            print("rat")
        elif a%12==2:
            print("ox")
        elif a%12==3:
            print("tiger")
        elif a%12==4:
            print("rabbit")
        elif a%12==5:
            print("dragon")
        elif a%12==6:
            print("snake")
        elif a%12==7:
            print("horse")
        elif a%12==8:
            print("goat")
        elif a%12==9:
            print("monkey")
        elif a%12==10:
            print("rooster")
        elif a%12==11:
            print("dog")
        elif a%12==0:
            print("pig")
getZodiac(1970)
