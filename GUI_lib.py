import PySimpleGUI as sg

 

def filebrowser(theme):

    sg.theme(theme)

    layout = [[sg.T("")],

              [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],

              [sg.Button("Submit")]]

    ###Building Window

    window = sg.Window('File Selection', layout, size=(600,150))

       

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event=="Exit":

            break

        elif event == "Submit":

            #print(values["-IN-"])

            window.close()

            return (values["-IN-"])

 

 

 

 

def folderbrowser(theme):

    sg.theme(theme)

    layout = [[sg.T("")], [sg.Text("Choose a folder: "), sg.Input(), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")]]

   

    ###Building Window

    window = sg.Window('Folder Selection', layout, size=(600,150))

       

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event=="Exit":

            break

        elif event == "Submit":

           #print(values["-IN-"])

            window.close()  

            return (values["-IN-"])

           

 

 