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
main.title("Image Encrypt Decrypt")
main.minsize(800, 400)
main.maxsize(800, 400)
main.labelFrame = Label(main, text = "Open File:", font=('Impact', -20), bg='#000', fg='#000')
main.labelFrame.grid(column = 0, row = 2, padx = 20, pady = 20)
main.configure(background='#dfdddd')
main.labelFrame.configure(background='#dfdddd')

def registerme():
    registeruser.regme()

def signinme():
    third_face_recognition.testme()



def register():
        main.showoriginal = Button(main, text = "Register",command = registerme)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 0, row = 3)

def signin():
        main.showoriginal = Button(main, text = "Signin",command = signinme)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 1, row = 3)

register()
signin()
main.mainloop()
