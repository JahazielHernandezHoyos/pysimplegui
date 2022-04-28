import PySimpleGUI as sg
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Ingrese')],
            [sg.Text('Documento de identidad'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout, default_element_size=(40, 1))
# Event Loop to process "events"
while True:             
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break

window.Close()