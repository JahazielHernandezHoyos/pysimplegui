import PySimpleGUI as sg


layout = [
    [sg.Image(filename='logo.png')],
    [sg.Text('Bienvenido', font=('Helvetica', 25), justification='center')],
    [sg.Text("*Si es tu primera vez usando el sistema de asistencia por favor seleccione, 'Registro nuevo' de lo contrario 'Enviar Asistencia'", font=('Helvetica', 12), text_color='blue')],
    [sg.Button('Registro nuevo', font=('Helvetica', 18)), sg.Button('Enviar Asistencia', font=('Helvetica', 18))],
    [sg.Text('', size=(20, 1), font=('Helvetica', 18), text_color='red', key='out')]]

window = sg.Window('Tecnoacademia', layout, default_button_element_size=(
    15, 2), auto_size_buttons=False, element_justification='c')
window.Maximize

event, values = window.read()    
window.close()