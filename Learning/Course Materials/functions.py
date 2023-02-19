FILEPATH = "Files/Todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the
    to-do items"""
    with open(filepath, "r") as file:  # #using context manager (with function)
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):    # Creating a function to reduce the number of repetition in code
    """write a to-do item in a text
    file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")
