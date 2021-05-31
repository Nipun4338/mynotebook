from tkinter import *
import tkinter
import first_face_dataset, registeruser, second_face_training
import mysql.connector
import tkinter.scrolledtext as scrolledtext
from fpdf import FPDF
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import ttk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="mynotebook"
)

def delete(*values):
    mycursor = mydb.cursor()
    sql="Delete from user"+str(values[0])+" where id='"+str(values[1])+"'"
    mycursor.execute(sql)
    mydb.commit()
    mycursor = mydb.cursor()
    sql="Delete from images where note_id='"+str(values[1])+"'"
    mycursor.execute(sql)
    mydb.commit()
    alert=Tk()
    alert.title('Successfull!')
    alert.minsize(800, 400)
    alert.maxsize(800, 400)
    Label(alert, text = "Successfully Deleted!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)


def update(*values):
    if len(values[0])>0 and len(values[1])>0:
        mycursor = mydb.cursor()
        sql="Update user"+str(values[2])+" set subject='"+str(values[1])+"',note='"+str(values[0])+"' where id='"+str(values[3])+"'"
        mycursor.execute(sql)
        mydb.commit()
        alert=Tk()
        alert.title('Successfull!')
        alert.minsize(800, 400)
        alert.maxsize(800, 400)
        Label(alert, text = "Successfully Updated!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)
    else:
        alert=Tk()
        alert.title('Alert')
        alert.minsize(800, 400)
        alert.maxsize(800, 400)
        Label(alert, text = "Nothing to update due to empty!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)


def update_text(*values):
    noteedit=Tk()
    noteedit.title('Edit Notes')
    mycursor = mydb.cursor()
    sql="SELECT * FROM user"+str(values[2])+" where id="+str(values[3])
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==0:
                e = Label(noteedit,width=15, text=student[j],
                borderwidth=2,relief='ridge', anchor="w",font=('Impact', -20), bg='#fff', fg='#000')
                e.pack(side=TOP, anchor=NW)
                e.config(anchor=CENTER)
            if j==2:
                e = Label(noteedit,width=25, text=student[j].strftime("%c"),
                borderwidth=2,relief='ridge', anchor="w",font=('Impact', -20), bg='#fff', fg='#000')
                e.pack(side=TOP, anchor=NE)
                e.config(anchor=CENTER)

    sub = Entry(noteedit,font='Arial 18', fg='Grey', width=50)
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==1:
                sub.insert(tkinter.INSERT,student[j])
    sub.pack(side=TOP, anchor=NW)

    txt = scrolledtext.ScrolledText(noteedit, undo=True)
    txt['font'] = ('consolas', '12')
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==3:
                txt.insert(tkinter.INSERT,student[j])
    txt.pack(expand=True, fill='both')
    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.config(borderwidth=3, relief="sunken")
    btn = tkinter.Button(noteedit,width=15, text="Update", command= lambda:[update(txt.get('1.0', 'end-1c'),str(sub.get()),values[2], values[3])],fg="#456")
    btn.pack()


def get_text(*values):
    if len(values[0])>0 and len(values[1])>0:
        mycursor = mydb.cursor()
        sql="Insert into user"+str(values[2])+" (subject,note) values('"+str(values[1])+"','"+str(values[0])+"')"
        mycursor.execute(sql)
        mydb.commit()
        alert=Tk()
        alert.title('Successfull!')
        alert.minsize(800, 400)
        alert.maxsize(800, 400)
        Label(alert, text = "Successfully Inserted!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)
    else:
        alert=Tk()
        alert.title('Alert')
        alert.minsize(800, 400)
        alert.maxsize(800, 400)
        Label(alert, text = "Nothing to insert due to empty!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)

def pdf(*values):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", style='B', size = 15)

    # create a cell
    pdf.cell(200, 10, txt = values[1],
             ln = 1, align = 'C')

    pdf.set_font("Helvetica", size = 15)
    #add images
    mycursor4 = mydb.cursor()
    sql4="SELECT * FROM images where note_id="+str(values[3])
    mycursor4.execute(sql4)

    if mycursor4:
        for images in mycursor4:
            for j in range(len(images)):
                if j==2:
                    pdf.image(name=images[j], x = None, y = None, w = 190, h = 100, type = '', link = '')

    # add another cell
    pdf.cell(200, 10, txt = values[0],
             ln = 2, align = 'C')


    # save the pdf with name .pdf
    pdf.output(str(values[2])+"-"+str(values[3])+".pdf")
    alert=Tk()
    alert.title('Successfull!')
    alert.minsize(800, 400)
    alert.maxsize(800, 400)
    Label(alert, text = "Successfully Saved!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)


def view_image(*values):
    novi = Toplevel()
    canvas = Canvas(novi, width = 600, height = 600)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = ImageTk.PhotoImage(file = values[0])
                                #image not visual
    canvas.create_image(0, 0, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1


def view(*values):
    noteview=Toplevel()
    noteview.title('Notes')
    mycursor = mydb.cursor()
    sql="SELECT * FROM user"+str(values[0])+" where id="+str(values[1])
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==0:
                e = Label(noteview,width=15, text=student[j],
                borderwidth=2,relief='ridge', anchor="w",font=('Impact', -20), bg='#fff', fg='#000')
                e.pack(side=TOP, anchor=NW)
                e.config(anchor=CENTER)
            if j==2:
                e = Label(noteview,width=25, text=student[j].strftime("%c"),
                borderwidth=2,relief='ridge', anchor="w",font=('Impact', -20), bg='#fff', fg='#000')
                e.pack(side=TOP, anchor=NE)
                e.config(anchor=CENTER)

    sub = Entry(noteview,font='Arial 18', fg='Grey', width=50)
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==1:
                sub.insert(tkinter.INSERT,student[j])
    sub.pack(side=TOP, anchor=NW)
    sub.config(state=DISABLED)

    mycursor4 = mydb.cursor()
    sql4="SELECT * FROM images where note_id="+str(values[1])
    mycursor4.execute(sql4)

    txt = scrolledtext.ScrolledText(noteview, undo=True)
    txt['font'] = ('consolas', '12')
    txt.pack(expand=True, fill='both')
    txt1=noteview
    counter=0
    if mycursor4:
        for images in mycursor4:
            for j in range(len(images)):
                if j==2:
                    counter+=1
                    txt1.showoriginal = Button(txt1,width=15, text = "View Image "+str(counter),command=lambda images=images: view_image(images[2]))
                    txt1.showoriginal.configure(background='#e28743')
                    txt1.showoriginal.pack()

    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==3:
                txt.insert(tkinter.INSERT,student[j])

    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.config(borderwidth=3, relief="sunken")
    txt.config(state=DISABLED)
    btn = tkinter.Button(noteview,width=15, text="Edit", command= lambda:[update_text(txt.get('1.0', 'end-1c'),str(sub.get()),values[0], values[1])],fg="#456")
    btn.pack()
    btn1 = tkinter.Button(noteview,width=15, text="Save as PDF", command= lambda:[pdf(txt.get('1.0', 'end-1c'),str(sub.get()),values[0], values[1])],fg="#456")
    btn1.pack()

def add_images(*values):
    mycursor1 = mydb.cursor()
    sql="SELECT * FROM user"+str(values[0])+" order by date desc limit 0,1"
    mycursor1.execute(sql)
    myresult = mycursor1.fetchone()
    if myresult:
        yourImage=filedialog.askopenfilenames(title = "Select your image",filetypes = [("Image Files","*.png"),("Image Files","*.jpg")])
        for i in yourImage:
            mycursor2 = mydb.cursor()
            id=myresult[0]+1
            sql=sql="Insert into images (note_id, path) values('"+str(id)+"','"+str(i)+"')"
            mycursor2.execute(sql)
            mydb.commit()
            alert=Tk()
            alert.title('Successfull!')
            alert.minsize(800, 400)
            alert.maxsize(800, 400)
            Label(alert, text = "Image Added!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)
    else:
        yourImage=filedialog.askopenfilenames(title = "Select your image",filetypes = [("Image Files","*.png"),("Image Files","*.jpg")])
        for i in yourImage:
            mycursor2 = mydb.cursor()
            id=1
            sql=sql="Insert into images (note_id, path) values('"+str(id)+"','"+str(i)+"')"
            mycursor2.execute(sql)
            mydb.commit()
            alert=Tk()
            alert.title('Successfull!')
            alert.minsize(800, 400)
            alert.maxsize(800, 400)
            Label(alert, text = "Image Added!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)


def addnew(*values):
    add=Tk()
    add.title('Add a new note')
    sub = Entry(add,font='Arial 18', fg='Grey', width=50)
    sub.insert(0, "Subject:")
    sub.pack(side=TOP, anchor=NW)

    txt = scrolledtext.ScrolledText(add, undo=True)
    txt['font'] = ('consolas', '12')
    txt.pack(expand=True, fill='both')
    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.config(borderwidth=3, relief="sunken")
    btn = tkinter.Button(add,width=15, text="Insert", command= lambda:[get_text(txt.get('1.0', 'end-1c'),str(sub.get()),values[0])],fg="#456")
    btn.pack()
    btn1 = tkinter.Button(add,width=15, text="Add Images", command= lambda:[add_images(values[0])],fg="#456")
    btn1.pack()




def myprofile(id):
    profile1=Tk()
    profile1.title('Profile')
    profile1.minsize(800, 400)
    profile1.maxsize(800, 400)
    Label(profile1, text = "Name: "+str(id)).grid(column= 0, row = 1)
    mycursor = mydb.cursor()
    sql="CREATE TABLE if not exists user"+str(id)+" (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, subject VARCHAR(255) NULL, note TEXT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NULL)"
    mycursor.execute(sql)
    sql="SELECT * FROM user"+str(id)+" order by date desc"
    mycursor.execute(sql)
    profile1.showoriginal = Button(profile1, text = "Add a new note", command=lambda:[addnew(id)])
    profile1.showoriginal.configure(background='#e28743')
    profile1.showoriginal.grid(column= 1, row = 1)
    e=Label(profile1,width=15,text='Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.config(anchor=CENTER)
    e.grid(row=4,column=0)
    e=Label(profile1,width=30,text='Subject',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.config(anchor=CENTER)
    e.grid(row=4,column=1)
    e=Label(profile1,width=20,text='Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.config(anchor=CENTER)
    e.grid(row=4,column=2)
    i=5
    for student in mycursor:
        for j in range(len(student)):
            if j==0:
                e = Label(profile1,width=15, text=student[j],
    	        borderwidth=2,relief='ridge', anchor="w")
                e.config(anchor=CENTER)
                e.grid(row=i, column=j)
            if j==1:
                e = Label(profile1,width=30, text=student[j],
    	        borderwidth=2,relief='ridge', anchor="w")
                e.config(anchor=CENTER)
                e.grid(row=i, column=j)
            if j==2:
                e = Label(profile1,width=20, text=student[j].strftime("%c"),
    	        borderwidth=2,relief='ridge', anchor="w")
                e.config(anchor=CENTER)
                e.grid(row=i, column=j)
            if j==3:
                profile1.showoriginal = Button(profile1,width=15, text = "View",command=lambda student=student: view(id,student[0]))
                profile1.showoriginal.configure(background='#e28743')
                profile1.showoriginal.grid(column= 4, row = i)
                profile1.showoriginal = Button(profile1,width=15, text = "Delete",command=lambda student=student: delete(id,student[0]))
                profile1.showoriginal.configure(background='#e28743')
                profile1.showoriginal.grid(column= 5, row = i)
        i=i+1




if __name__ == '__main__':
    # test1.py executed as script
    # do something
    myprofile(id)
