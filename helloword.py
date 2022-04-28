import PySimpleGUI as sg

sg.theme('Dark Grey 13')

def sumar(a, b):
    return a + b

layout = [[sg.Text('Filename')],
          [sg.Text("numero 1"), sg.Input(), sg.Text("numero 2"), sg.Input()],
          [sg.OK(), sg.Cancel()],
          [sg.Image(filename='logo.png')]]

window = sg.Window('Pruebas funciones', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'OK':
        sg.popup_ok(sumar(int(values[0]), int(values[1])))

window.close()