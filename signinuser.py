from tkinter import *
import first_face_dataset, registeruser, second_face_training
import mysql.connector


def signme():
    window2= Tk()
    window2.title('Register')
    window2.minsize(800, 400)
    window2.maxsize(800, 400)
    Label(window, text = "Enter Your Phone Number for Register:").grid(column= 0, row = 4)
    num1 = Entry(window)
    num1.grid(column= 1, row = 4)
    Ans = str(num1.get())
    window.video = Button(window, text = "Take video screen",command = lambda:[video(str(num1.get()))])
    window.video.configure(background='#e28743')
    window.video.grid(column= 2, row = 13)
    #first_face_dataset.takesample(Ans)


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    signme()
