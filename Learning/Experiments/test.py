def greet(message):
    new_message = message.title()
    return new_message


user_greeting = input("what greeting do you prefer:")
greeting = greet(user_greeting)
print(greeting)