waiting_list = ["sen","paul","ben"]
waiting_list = waiting_list.sort()

for index ,i in enumerate(waiting_list):
    row = f"{index + 1}-{i.capitalize()}"
    print(row)
