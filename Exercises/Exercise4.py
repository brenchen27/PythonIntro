def hotelCost(day):
    return 140*day



def planeCost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475



def rentalCarCost(day):
    if day<3:
        return 40*day
    elif day>7:
        return 40*day-50
    else:
        return 40*day-20



def tripCost(day, city):
    return hotelCost(day)+planeCost(city)+rentalCarCost(day)
print(tripCost(3,"Tampa"))
