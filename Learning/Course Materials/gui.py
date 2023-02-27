import functions

import PySimpleGUI as sg

label = sg.Text("Type in a todo".title())
input_box = sg.InputText(tooltip="Enter todo".title(),key="todo")
add_button = sg.Button("Add")

window = sg.Window("My Todo App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()
