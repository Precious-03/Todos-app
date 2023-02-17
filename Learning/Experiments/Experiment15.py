import glob

my_file = glob.glob("../junk/*.txt")


for filepath in my_file:
    with open(filepath, "r") as file:
        print(file.read())
