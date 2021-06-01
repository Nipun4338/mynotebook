from tkinter import *
import tkinter
import first_face_dataset, registeruser, second_face_training
import mysql.connector
import tkinter.scrolledtext as scrolledtext
from fpdf import FPDF
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import ttk
from datetime import datetime

#connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="mynotebook"
)

#view separate note images
def view_image(*values):
    novi = Toplevel()
    canvas = Canvas(novi, width = 600, height = 600)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = ImageTk.PhotoImage(file = values[0])
                                #image not visual
    canvas.create_image(0, 0, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1

#all photos
def galleryview(id):
    gallery=Tk()
    gallery.title("Gallery")

    main_frame=Frame(gallery)
    main_frame.pack(fill=BOTH, expand=1)

    gallery2=Canvas(main_frame,width = 920, height = 400)
    gallery2.pack(side=LEFT, fill=BOTH, expand=1)

    sb = ttk.Scrollbar(main_frame, orient=VERTICAL, command=gallery2.yview)
    sb.pack(side = RIGHT, fill = Y)
    gallery2.configure(yscrollcommand = sb.set )
    gallery2.bind('<Configure>', lambda e: gallery2.configure(scrollregion = gallery2.bbox("all")))
    gallery1=Frame(gallery2)
    gallery2.create_window((0,0), window=gallery1, anchor='nw')

    Label(gallery1, text = "Your Images", font=('Impact', -15),borderwidth=1, relief="raised", fg='#000').grid(column= 0, row = 1)

    mycursor = mydb.cursor()
    sql="SELECT * FROM images where user_id='"+str(id)+"'"
    mycursor.execute(sql)
    counter=0
    i=1
    flag1=0
    if mycursor:
        for student in mycursor:
            for j in range(len(student)):
                global flag
                flag=student[1]
                if flag!=flag1:
                    flag1=flag
                    i+=1
                    counter=0
                counter+=1
                if j==2:
                    gallery1.showoriginal = Button(gallery1,width=10, text = "Note "+str(student[1]),font=('Impact', -10),fg="#fff",command=lambda student=student: view_image(student[2]))
                    gallery1.showoriginal.configure(background='#f0ad4e')
                    gallery1.showoriginal.grid(column= counter, row = i)







if __name__ == '__main__':
    # test1.py executed as script
    # do something
    galleryview(id)
