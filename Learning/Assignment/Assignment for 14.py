Temperature = input("Kindly state the temperature of the water: ")


def state(Temperature):
    if int(Temperature) < 0:
        return "Solid"
    elif int(Temperature) > 0 and int(Temperature) < 100:
        return "liquid"
    else:
        return "Gas"


print(state(Temperature))