while True:
    result = input("head or tail or delete or exit:")
    match result:
        case "head":
            with open(f"../../Files/Keys.txt", "r") as file:
                records = file.readlines()

            records.append(result + "\n")

            with open(f"../../Files/Keys.txt", "w") as file:
                file.writelines(records)

                g = int(records.count("head\n"))
                s = int(records.count("tail\n"))
                probability = 100 * (g/(g+s))
                print(probability)

        case "tail":
            with open(f"../../Files/Keys.txt", "r") as file:
                records = file.readlines()

            records.append(result + "\n")

            with open(f"../../Files/Keys.txt", "w") as file:
                file.writelines(records)

                x = int(records.count("head\n"))
                w = int(records.count("tail\n"))
                probability_T = 100 - (100 * (w/(x+w)))
                print(probability_T)

        case "delete":
            with open(f"../../Files/Keys.txt", "r") as file:
                records = file.readlines()

            select_T = int(input("which entry: "))
            records_T = records.pop(select_T)

            with open(f"../../Files/Keys.txt", "w") as file:
                file.writelines(records)

        case "exit":
            break
























