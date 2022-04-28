import PySimpleGUI27 as sg

def registro():
    layout = [[sg.Text('Ingrese su documento de identidad')],
          [sg.Input(size=(15, 1), justification='center', key='input')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9')],
          [sg.Button('Enviar'), sg.Button('0'), sg.Button('Limpiar')],
          [sg.Button("Volver", font=('Helvetica', 15))]]

    window = sg.Window('Keypad', layout, default_button_element_size=(15,2), auto_size_buttons=False, element_justification='c', no_titlebar=True, location=(0,0), size=(800,600), keep_on_top=True).Finalize()

    # Loop forever reading the window's values, updating the Input field
    keys_entered = ''
    while True:
        event, values = window.read()  # read the window
        if event == 'Volver': 
            window.close()
            ventanaPrincipal()
        if event == 'Limpiar':  # clear keys if clear button
            keys_entered = ''
        elif event in '1234567890':
            keys_entered = values['input']  # get what's been entered so far
            keys_entered += event  # add the new digit
        elif event == 'Enviar':
            keys_entered = values['input']
            window.close()
            sg.popup_ok(keys_entered, no_titlebar=True, location=(0,0), size=(800,600), keep_on_top=True)
            ventanaPrincipal()
        window['input'].update(keys_entered)  # change the window to reflect current key string   
        

def verificarUsuario():
    layout = [[sg.Text('Pon tu dedo en el lector de huellas')],
        #   [sg.Image(filename='/home/pi/Desktop/codigo de pruebas/pysimplegui-master/correcta.png')],
          [sg.Button("Volver", font=('Helvetica', 18))],
          [sg.Button("Enviar", font=('Helvetica', 18))]]
    window = sg.Window('Keypad', layout, default_button_element_size=(15,2), auto_size_buttons=False, element_justification='c', no_titlebar=True, location=(0,0), size=(800,600), keep_on_top=True).Finalize()
    event, values = window.read()  # read the window
    if event == "Enviar":
        VerifyUser()
        print("s")
        window.close()
        sg.popup_ok("Tu asistencia ha sido enviada", no_titlebar=True, location=(0,0), size=(800,600), keep_on_top=True)
        ventanaPrincipal()
    if event == 'Volver': 
        window.close()
        ventanaPrincipal()

def ventanaPrincipal():
    layout = [
        # [sg.Image(filename='/home/pi/Desktop/codigo de pruebas/pysimplegui-master/logo.png')],
        [sg.Text('Bienvenido', font=('Helvetica', 25), justification='center')],
        [sg.Text("*Para iniciar el proceso de click en Verificar", font=('Helvetica', 12), text_color='blue')]]

    window = sg.Window('Tecnoacademia', layout, default_button_element_size=(
        15, 2), auto_size_buttons=False, element_justification='c', no_titlebar=True, location=(0,0), size=(800,600), keep_on_top=True).Finalize()

    event, values = window.read()
    if event == "Registro nuevo":
        window.close()
        registro()
    if event == "Verificar":
        window.close()
        verificarUsuario()

ventanaPrincipal()