import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from PIL import Image, ImageTk
import numpy as np
from tkinter.font import Font
from tkinter.messagebox import *
import time
import first_face_dataset, registeruser, third_face_recognition

image1=''
main = Tk()
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
print(cwd)
os.chdir(dir_path)
main.bold_font = Font(family="Helvetica", size=14, weight="bold")
main.title("My Notebook")
main.minsize(400, 200)
main.maxsize(400, 200)
main.labelFrame = Label(main, text = "Welcome to Notebook", font=('Impact', -20), bg='#000', fg='#000')
main.labelFrame.place(relx = 0.5,
                   rely = 0.2,
                   anchor = 'center')
main.configure(background='#dfdddd')
main.labelFrame.configure(background='#dfdddd')

def registerme():
    registeruser.regme()

def signinme():
    third_face_recognition.testme()



def register():
        main.showoriginal = Button(main, text = "Register",command = registerme)
        main.showoriginal.configure(background='#df4759',font=('Impact', -20),fg='#fff')
        main.showoriginal.place(relx = 0.37,
                           rely = 0.5,
                           anchor = 'center')

def signin():
        main.showoriginal = Button(main, text = "Sign-in",command = signinme)
        main.showoriginal.configure(background='#42ba96',font=('Impact', -20),fg='#fff')
        main.showoriginal.place(relx = 0.63,
                           rely = 0.5,
                           anchor = 'center')

register()
signin()
main.mainloop()
