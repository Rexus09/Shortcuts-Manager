import tkinter
from tkinter import *
from tkinter import messagebox
import time
import webbrowser
#Define
historial = []
root = Tk()
root.geometry("1080x720")
root.title("Shortcuts Administer")
#Esconder todo
def hideall():
    #Introducir la contraseña
    confirm_button.grid_forget()
    label_start.grid_forget()
    input_field_password.grid_forget()

    #Pantalla 1
    label_superior.grid_forget()
    label_start.grid_forget()
    label.grid_forget()
    label_2.grid_forget()
    label_3.grid_forget()
    label_4.grid_forget()
    label_5.grid_forget()
    label_6.grid_forget()
    label_7.grid_forget()
    label_8.grid_forget()
    label_9.grid_forget()
    label_10.grid_forget()
    escape_button.grid_forget()

    #Pantalla 2
    b2label_1.grid_forget()
    b2label_2.grid_forget()
    b2label_3.grid_forget()
    b2label_4.grid_forget()
    b2label_5.grid_forget()
    b2label_6.grid_forget()
    b2label_7.grid_forget()
    b2label_8.grid_forget()
    b2label_9.grid_forget()
    b2label_10.grid_forget()
    b2escape_button.grid_forget()    
    b2label_superior.grid_forget()

def open_classroom():
    webbrowser.open("https://classroom.google.com/u/0/")
#Pantalla 1, Clase
label_superior = Label(root, text = "Class Accesses:")
label_2 = Button(root, text = "Web1",bg = "blue")
label = Button(root, text = "Classroom",bg = "red", command = open_classroom )        
label_3 = Button(root, text = "2 Web",bg = "green")
label_4 = Button(root, text = "3 Web",bg = "yellow")        
label_5 = Button(root, text = "4 Web",bg = "brown")        
label_6 = Button(root, text = "5 Web",bg = "pink")
label_7 = Button(root, text = "6 Web",bg = "white")        
label_8 = Button(root, text = "7 Web",bg = "black", fg = "white")        
label_9 = Button(root, text = "8 Web",bg = "purple")
label_10 = Button(root, text = "9 Web",bg = "orange")        

def activation01():
    hideall()
    label_superior.grid(row = 1, column = 1)
    label.grid(row = 2 ,column = 3)
    label_2.grid(row = 4 ,column = 3)
    label_3.grid(row = 6 ,column = 3)
    label_4.grid(row = 8 ,column = 3)
    label_5.grid(row = 10 ,column = 3)
    label_6.grid(row = 12 ,column = 3)
    label_7.grid(row = 14 ,column = 3)
    label_8.grid(row = 16 ,column = 3)
    label_9.grid(row = 18, column = 3)
    label_10.grid(row = 20, column = 3)
    escape_button.grid(row = 1, column = 5)
def open_brave():
    webbrowser.open("https://duckduckgo.com/?q=&t=brave")
def open_gmail():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
def open_proton():
    webbrowser.open("https://mail.protonmail.com/inbox")
def open_mega():
    webbrowser.open("https://mega.nz/fm/ygxQ3YYJ")
def open_stack():
    webbrowser.open("https://stackoverflow.com/")
def open_git():
    webbrowser.open("https://github.com/")
def open_youtube():
    webbrowser.open("https://www.youtube.com/")
def open_reddit():
    webbrowser.open("https://www.reddit.com/")

#Pantalla 2,Personal
b2label_superior = Label(root, text = "Access Personal:")
b2label_1 = Button(root, text = "Duck Duck ", command = open_brave)
b2label_2 = Button(root, text = "Gmail", command = open_gmail)        
b2label_3 = Button(root, text = "Protonmail", command = open_proton)
b2label_4 = Button(root, text = "Mega", command = open_mega )     
b2label_5 = Button(root, text = "Stack Overflow",command = open_stack)        
b2label_6 = Button(root, text = "Github", command = open_git)
b2label_7 = Button(root, text = "Youtube",command = open_youtube)        
b2label_8 = Button(root, text = "Reddit", command = open_reddit)        
b2label_9 = Button(root, text = "9 Web")
b2label_10 = Button(root, text = "10 Web")             
def activation02():  
    global historial  
    historial.append(2)
    hideall()
    b2label_superior.grid(row = 1, column = 1)
    b2label_1.grid(row = 2 ,column = 3)
    b2label_2.grid(row = 4 ,column = 3)
    b2label_3.grid(row = 6 ,column = 3)
    b2label_4.grid(row = 8 ,column = 3)
    b2label_5.grid(row = 10 ,column = 3)
    b2label_6.grid(row = 12 ,column = 3)
    b2label_7.grid(row = 14 ,column = 3)
    b2label_8.grid(row = 16 ,column = 3)
    b2label_9.grid(row = 18, column = 3)
    b2label_10.grid(row = 20, column = 3)
    b2escape_button.grid(row = 1, column = 5)

#Menu de seleccion
def mainmenu():
    historial.append(4)
    hideall()
    global button_clase
    button_clase = Button(root, text = "Class", command = activation01).grid(row =2 , column = 1)
    global button_personal
    button_personal = Button(root, text = "Personal", command = activation02).grid(row =2 , column = 2)

b2escape_button = Button(root, text = "Back", command = mainmenu)
escape_button = Button(root, text = "Back", command = mainmenu)
############################################################################################################################################################
############################  MODIFY HERE YOUR PASSWORD  ###################################################################################################
############################################################################################################################################################
#Edit the passwor by changing that 1234 number, keep whatever your password is the brackets 
def dotget():    
    if input_field_password.get() ==  "1234":
        mainmenu()
        confirm_button.grid_forget()
        label_start.grid_forget()
        input_field_password.grid_forget()
    else:
        print("Wrong Answer :(")      
        
#Pantalla 0, menu principal
input_field_password = Entry(root, bg = "white")
label_start = Label(root, text = "Password", fg = "Black")
confirm_button = Button(root, text = "Confirm", command = dotget )    

##Mostrar los 3 botones en los que se mete la contraseña
def passmenu():
    hideall()
    input_field_password.grid(row = 1, column = 3)
    label_start.grid(row = 1, column = 1)
    confirm_button.grid(row = 2, column = 2)

passmenu()

mainloop()
#To add your shortcuts, just edit the code as i did with the buttons, after renaming the button you want to create
#a shortcut, add: , command = open_your_web
#then go below the button definition and define the function like the others:
#def open_your_web():
#    webbrowser.open("Your Url")