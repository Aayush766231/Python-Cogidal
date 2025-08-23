def hotelCost(night):
    return 140*night
def planeRide(city):
    if city == "Charlotte":
        return 183
    elif city == "Pittsburgh":
        return 200
    elif city == "Tampa":
        return 250
    elif city == "LA":
        return 300
def rentalCar(days):
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days - 50
    else:
        return 40*days
def totalCost(days, city, money):
    return hotelCost(days) + rentalCar(days) + planeRide(city) + money

print("For 5 nights, a hotel will cost", hotelCost(5))
print("For 5 days, a rental car will cost", rentalCar(5))
print(f"Going to Tampa costs {planeRide("Tampa")}")
print(f"A 7 day trip to LA costs {totalCost(7, "LA", 200)}")