import functions

import PySimpleGUI as sg

label = sg.Text("Type in a todo".title())
input_box = sg.InputText(tooltip="Enter todo".title(), key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[30,10])

edit_button = sg.Button("Edit")

window = sg.Window("My Todo App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Courier new", 12))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)

        case "Edit":
            todos_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todos_to_edit)

            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
