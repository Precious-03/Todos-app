from Modules.functions import get_todos, write_todos
import time


now = time.strftime("%b %d,%Y  %H:%M:%S")
print("It is", now)

while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()                        # #to remove unnecessary spacing
    user_action = user_action.lower()

    if user_action.startswith("add"):
            Todo = user_action[4:]

            Todos = get_todos()

            Todos.append(Todo + "\n")

            write_todos(Todos)

    elif user_action.startswith("show"):

            Todos = get_todos()

            #  #show_Todos = [item.strip("\n") for item in Todos]"
            # #list comprehension could be used to remove the double-spacing in outputs when displayed

            for index, item in enumerate(Todos):
                item = item.strip("\n")
                row = f"{int(index)+1}-{item.title()}"  # using the F-string to concatenate index and item
                print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            Todos = get_todos()

            new_todo = input("Enter new Todo: ")  # #todo variable to make inputs editable
            Todos[number] = new_todo + "\n"

            write_todos(Todos)

        except ValueError:
            print("Error with input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            Todos = get_todos()

            Index = number-1
            Todo_to_be_removed = Todos[Index]
            Todos.pop(number - 1)

            write_todos(Todos)

            message = f"the deleted todo from the list is {Todo_to_be_removed}"
            print(message)
        except IndexError:
            print("Todo not found")
            continue
        except ValueError:
            print("Error with input")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Option not recognised enter a valid option")

print("Thanks")