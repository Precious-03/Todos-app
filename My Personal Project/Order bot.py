Menu = {"Hamburger": 3.5, "Ice chocolate": 3, "Bottle water": 1, "Onions rings": 2.5}
Order = []
Cost_list = []
Username = input("Welcome, Please state a name: ")
print(f"Welcome {Username.capitalize()}")

while True:
    Order_g = input("Kindly state your order: ")

    Order_list = Order.append(Order_g)

    for item in Order:
        Value = Menu.get(item)
    Cost_list1 = Cost_list.append(Value)

    if Order_g == "end":
        Cost = sum(Cost_list[:-1])
        print(f"Purchased {[item for item in Order[:-1]]}")
        print(Cost)
        break








