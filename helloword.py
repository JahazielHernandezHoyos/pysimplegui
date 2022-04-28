import PySimpleGUI as sg

sg.theme('Dark Grey 13')

def sumar(a, b):
    return a + b

layout = [[sg.Text('Filename')],
          [sg.Text("numero 1"), sg.Input(), sg.Text("numero 2"), sg.Input()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout)

event, values = window.read()
if event == 'OK':
    sumar(values[0], values[1])
    

window.close()