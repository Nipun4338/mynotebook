from tkinter import *
import tkinter
import first_face_dataset, registeruser, second_face_training, gallery
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

#delete note
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
    alert.minsize(200, 50)
    alert.maxsize(200, 50)
    alert.configure(background='#456')
    Label(alert, text = "Successfully Deleted!",font=('Impact', -20),bg='#456',fg="#42ba96").place(relx = 0.5,
                       rely = 0.5,
                       anchor = 'center')


#update note
def update(*values):
    if len(values[0])>0 and len(values[1])>0:
        mycursor = mydb.cursor()
        sql="Update user"+str(values[2])+" set subject='"+str(values[1])+"',note='"+str(values[0])+"' where id='"+str(values[3])+"'"
        mycursor.execute(sql)
        mydb.commit()
        alert=Tk()
        alert.title('Successfull!')
        alert.minsize(400, 50)
        alert.maxsize(400, 50)
        alert.configure(background='#456')
        Label(alert, text = "Successfully Updated!",font=('Impact', -20),bg='#456',fg="#42ba96").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')
    else:
        alert=Tk()
        alert.title('Alert')
        alert.minsize(800, 400)
        alert.maxsize(800, 400)
        alert.configure(background='#fff')
        Label(alert, text = "Nothing to update due to empty!",font=('Impact', -20),bg='#fff',fg="#df4759").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')


#update note function call
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
                date_time=datetime.strptime(str(student[j]), '%Y-%m-%d %H:%M:%S')
                d = date_time.strftime("%d %B, %Y")
                d+=", "
                d+= date_time.strftime("%I:%M:%S %p")
                e = Label(noteedit,width=30, text=str(d),
                borderwidth=2,relief='ridge', anchor="w",font=('Impact', -20), bg='#fff', fg='#000')
                e.pack(side=TOP, anchor=NE)
                e.config(anchor=CENTER)

    sub = Entry(noteedit,font = ('courier', 15, 'bold'), width=50,foreground = 'green',borderwidth=15, relief=tkinter.SUNKEN)
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==1:
                sub.insert(tkinter.INSERT,student[j])
    sub.pack(side=TOP, anchor=NW,expand=True, fill='both')

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
    btn = tkinter.Button(noteedit,width=15, text="Update",font=('Impact', -20),fg='#fff', command= lambda:[update(txt.get('1.0', 'end-1c'),str(sub.get()),values[2], values[3])])
    btn.configure(background='#5bc0de')
    btn.pack()


#get text for inserting note
def get_text(*values):
    if len(values[0])>0 and len(values[1])>0:
        mycursor = mydb.cursor()
        sql="Insert into user"+str(values[2])+" (subject,note) values('"+str(values[1])+"','"+str(values[0])+"')"
        mycursor.execute(sql)
        mydb.commit()
        alert=Tk()
        alert.title('Successfull!')
        alert.minsize(400, 50)
        alert.maxsize(400, 50)
        alert.configure(background='#456')
        Label(alert, text = "Note Added!",font=('Impact', -20),bg='#456',fg="#42ba96").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')
    else:
        alert=Tk()
        alert.title('Alert')
        alert.minsize(400, 50)
        alert.maxsize(400, 50)
        alert.configure(background='#fff')
        Label(alert, text = "Nothing to add due to empty!",bg="#fff",font=('Impact', -20),fg="#df4759").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')

#save as pdf
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
    sql4="SELECT * FROM images where note_id='"+str(values[3])+"' and user_id='"+str(values[2])+"'"
    mycursor4.execute(sql4)

    if mycursor4:
        for images in mycursor4:
            for j in range(len(images)):
                if j==2:
                    im = Image.open(images[j])
                    width, height = im.size
                    pdf.image(name=images[j], x = None, y = None, w = 190, h = 100, type = '', link = '')

    # add another cell
    pdf.cell(200, 10, txt = values[0],
             ln = 2, align = 'C')


    # save the pdf with name .pdf
    pdf.output(str(values[2])+"-"+str(values[3])+".pdf")
    alert=Tk()
    alert.title('Successfull!')
    alert.minsize(200, 50)
    alert.maxsize(200, 50)
    alert.configure(background='#456')
    Label(alert, text = "Successfully Saved!",font=('Impact', -20),bg='#456',fg="#42ba96").place(relx = 0.5,
                       rely = 0.5,
                       anchor = 'center')


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


#view note
def view(*values):
    noteview=Tk()
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
                date_time=datetime.strptime(str(student[j]), '%Y-%m-%d %H:%M:%S')
                d = date_time.strftime("%d %B, %Y")
                d+=", "
                d+= date_time.strftime("%I:%M:%S %p")
                e = Label(noteview,width=30, text=str(d),
                borderwidth=2,relief='ridge', anchor="w",font=('Impact', -20), bg='#fff', fg='#000')
                e.pack(side=TOP, anchor=NE)
                e.config(anchor=CENTER)

    sub = Entry(noteview,font = ('courier', 15, 'bold'), width=50,foreground = 'green',borderwidth=15, relief=tkinter.SUNKEN)
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==1:
                sub.insert(tkinter.INSERT,student[j])
    sub.pack(side=TOP, anchor=NW,expand=True, fill='both')
    sub.config(state=DISABLED)

    mycursor4 = mydb.cursor()
    sql4="SELECT * FROM images where note_id='"+str(values[1])+"' and user_id='"+str(values[0])+"'"
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
                    txt1.showoriginal = Button(txt1,width=10, text = "View Image "+str(counter),font=('Impact', -10),fg="#fff",command=lambda images=images: view_image(images[2]))
                    txt1.showoriginal.configure(background='#f0ad4e')
                    txt1.showoriginal.pack(side=tkinter.RIGHT)

    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==3:
                txt.insert(tkinter.INSERT,student[j])

    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.config(borderwidth=5, relief="sunken")
    txt.config(state=DISABLED)
    btn = tkinter.Button(noteview,width=15, text="Edit",font=('Impact', -20),fg='#fff', command= lambda:[update_text(txt.get('1.0', 'end-1c'),str(sub.get()),values[0], values[1])])
    btn.configure(background='#5cb85c')
    btn.pack()
    btn1 = tkinter.Button(noteview,width=15, text="Save as PDF", font=('Impact', -20),fg='#fff', command= lambda:[pdf(txt.get('1.0', 'end-1c'),str(sub.get()),values[0], values[1])])
    btn1.configure(background='#0275d8')
    btn1.pack()

#inserting images
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
            sql=sql="Insert into images (note_id, path, user_id) values('"+str(id)+"','"+str(i)+"','"+str(values[0])+"')"
            mycursor2.execute(sql)
            mydb.commit()
        alert=Tk()
        alert.title('Successfull!')
        alert.minsize(200, 50)
        alert.maxsize(200, 50)
        alert.configure(background='#456')
        Label(alert, text = "Image Added!",font=('Impact', -20),bg='#456',fg="#42ba96").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')
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
        alert.minsize(200, 50)
        alert.maxsize(200, 50)
        alert.configure(background='#456')
        Label(alert, text = "Image Added!",font=('Impact', -20),bg='#456',fg="#42ba96").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')


#add new note
def addnew(*values):
    add=Tk()
    add.title('Add a new note')
    sub = Entry(add,font = ('courier', 15, 'bold'), width=50,foreground = 'green',borderwidth=15, relief=tkinter.SUNKEN)
    sub.insert(0, "Subject:")
    sub.pack(side=TOP, anchor=NW,expand=True, fill='both')

    txt = scrolledtext.ScrolledText(add, undo=True)
    txt['font'] = ('consolas', '12')
    txt.pack(expand=True, fill='both')
    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.config(borderwidth=5, relief="sunken")
    add.showoriginal = tkinter.Button(add,width=15, text="Insert",font=('Impact', -20),fg='#fff', command= lambda:[get_text(txt.get('1.0', 'end-1c'),str(sub.get()),values[0])])
    add.showoriginal.configure(background='#5cb85c')
    add.showoriginal.pack()
    add.showoriginal1 = tkinter.Button(add,width=15, text="Add Images",font=('Impact', -20),fg='#fff', command= lambda:[add_images(values[0])])
    add.showoriginal1.configure(background='#0275d8')
    add.showoriginal1.pack()


#Gallery
def gallerygo(values):
    gallery.galleryview(values)


#profile function
def myprofile(id):
    profile=Tk()
    profile.title("Profile")

    main_frame=Frame(profile)
    main_frame.pack(fill=BOTH, expand=1)

    profile2=Canvas(main_frame,width = 920, height = 400)
    profile2.pack(side=LEFT, fill=BOTH, expand=1)

    sb = ttk.Scrollbar(main_frame, orient=VERTICAL, command=profile2.yview)
    sb.pack(side = RIGHT, fill = Y)
    profile2.configure(yscrollcommand = sb.set )
    profile2.bind('<Configure>', lambda e: profile2.configure(scrollregion = profile2.bbox("all")))
    profile1=Frame(profile2)
    profile2.create_window((0,0), window=profile1, anchor='nw')


    Label(profile1, text = "Name: "+str(id), font=('Impact', -15),borderwidth=1, relief="raised", fg='#000').grid(column= 0, row = 1)
    mycursor = mydb.cursor()
    sql="CREATE TABLE if not exists user"+str(id)+" (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, subject VARCHAR(255) NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NULL, note TEXT NULL)"
    mycursor.execute(sql)
    sql="SELECT * FROM user"+str(id)+" order by date desc"
    mycursor.execute(sql)
    profile1.showoriginal = Button(profile1, text = "Add a new note",font=('Impact', -15), fg='#fff', command=lambda:[addnew(id)])
    profile1.showoriginal.configure(background='#5bc0de')
    profile1.showoriginal.grid(column= 1, row = 1)
    profile1.showoriginal = Button(profile1, text = "Refresh",font=('Impact', -15), fg='#fff', command=lambda:[myprofile(id)])
    profile1.showoriginal.configure(background='#ffff00')
    profile1.showoriginal.grid(column= 3, row = 1)
    profile1.showoriginal = Button(profile1, text = "Gallery",font=('Impact', -15), fg='#fff', command=lambda:[gallerygo(id)])
    profile1.showoriginal.configure(background='#16ca60')
    profile1.showoriginal.grid(column= 2, row = 1)
    e=Label(profile1,width=15,text='Id',borderwidth=3, relief='ridge',anchor='w',bg='yellow',font=('Impact', -15), fg='#000')
    e.config(anchor=CENTER)
    e.grid(row=4,column=0)
    e=Label(profile1,width=50,text='Subject',borderwidth=3, relief='ridge',anchor='w',bg='yellow',font=('Impact', -15), fg='#000')
    e.config(anchor=CENTER)
    e.grid(row=4,column=1)
    e=Label(profile1,width=30,text='Date',borderwidth=3, relief='ridge',anchor='w',bg='yellow',font=('Impact', -15), fg='#000')
    e.config(anchor=CENTER)
    e.grid(row=4,column=2)
    i=5
    for student in mycursor:
        for j in range(len(student)):
            if j==0:
                e = Label(profile1,width=15, text=student[j],fg='#000',bg='#fff',
    	        borderwidth=3,relief='ridge', anchor="w",font=('Impact', -15))
                e.config(anchor=CENTER)
                e.grid(row=i, column=j)
            if j==1:
                e = Label(profile1,width=50, text=student[j],fg='#000',bg='#fff',
    	        borderwidth=3,relief='ridge', anchor="w",font=('Impact', -15))
                e.config(anchor=CENTER)
                e.grid(row=i, column=j)
            if j==2:
                date_time=datetime.strptime(str(student[j]), '%Y-%m-%d %H:%M:%S')
                d = date_time.strftime("%d %B, %Y")
                d+=", "
                d+= date_time.strftime("%I:%M:%S %p")
                e = Label(profile1,width=30, text=str(d),fg='#000',bg='#fff',
    	        borderwidth=3,relief='ridge', anchor="w",font=('Impact', -15))
                e.config(anchor=CENTER)
                e.grid(row=i, column=j)
            if j==3:
                profile1.showoriginal = Button(profile1,width=15, text = "View",font=('Impact', -15),fg='#fff',command=lambda student=student: view(id,student[0]),cursor="mouse")
                profile1.showoriginal.configure(background='#5cb85c')
                profile1.showoriginal.grid(column= 3, row = i)
                profile1.showoriginal = Button(profile1,width=15, text = "Delete",font=('Impact', -15),fg='#fff',command=lambda student=student: delete(id,student[0]),cursor="pirate")
                profile1.showoriginal.configure(background='#d9534f')
                profile1.showoriginal.grid(column= 4, row = i)
        i=i+1





if __name__ == '__main__':
    # test1.py executed as script
    # do something
    myprofile(id)
