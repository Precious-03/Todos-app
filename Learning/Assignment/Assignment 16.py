import PySimpleGUI as sg

Label1 = sg.Text("Enter feet")
Input1 = sg.Input()
Label2 = sg.Text("Enter in Inches")
Input2 = sg.Input()

add_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[Label1, Input1], [Label2, Input2], [add_button]])
window.read()
window.close()