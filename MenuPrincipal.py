import PySimpleGUI as sg

logo = "logo.png"

layout = [
    [sg.Image(image_filename=logo)],
    [sg.Text("Bienvenido a la tecnoacademia si es tu primera vez usando el sistema de asistencia por favor seleccione, 'Registro nuevo' de lo contrario 'Enviar Asistencia'")],
    [sg.Button('Registro nuevo'), sg.Button('Enviar Asistencia')],
    [sg.Text('', size=(30, 3), font=('Helvetica', 18), text_color='red', key='out')]]

window = sg.Window('Tecnoacademia', layout, default_button_element_size=(
    15, 2), auto_size_buttons=False, element_justification='c')

event, values = window.read()    
window.close()