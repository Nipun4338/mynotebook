from tkinter import *
import tkinter
import first_face_dataset, registeruser, second_face_training
import mysql.connector
import tkinter.scrolledtext as scrolledtext

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="mynotebook"
)

def get_text(*values):
    if len(values[0])>0 and len(values[1])>0:
        mycursor = mydb.cursor()
        sql="Insert into user"+str(values[2])+" (subject,note) values('"+str(values[1])+"','"+str(values[0])+"')"
        print(sql)
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
                e = Label(noteview,width=20, text=student[j],
                borderwidth=2,relief='ridge', anchor="w",font=('Impact', -20), bg='#fff', fg='#000')
                e.pack(side=TOP, anchor=NE)
                e.config(anchor=CENTER)

    txt = scrolledtext.ScrolledText(noteview, undo=True)
    txt['font'] = ('consolas', '12')
    mycursor.execute(sql)
    for student in mycursor:
        for j in range(len(student)):
            if j==3:
                txt.insert(tkinter.INSERT,student[j])
    txt.pack(expand=True, fill='both')
    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.config(borderwidth=3, relief="sunken")
    txt.config(state=DISABLED)



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
    btn = tkinter.Button(add, text="Insert", command= lambda:[get_text(txt.get('1.0', 'end-1c'),str(sub.get()),values[0])])
    btn.pack()


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
    e=Label(profile1,width=15,text='Subject',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.config(anchor=CENTER)
    e.grid(row=4,column=1)
    e=Label(profile1,width=15,text='Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.config(anchor=CENTER)
    e.grid(row=4,column=2)
    i=5
    for student in mycursor:
        for j in range(len(student)):
            if j!=3:
                e = Label(profile1,width=15, text=student[j],
    	        borderwidth=2,relief='ridge', anchor="w")
                e.config(anchor=CENTER)
                e.grid(row=i, column=j)
            if j==3:
                profile1.showoriginal = Button(profile1,width=15, text = "View",command=lambda student=student: view(id,student[0]))
                profile1.showoriginal.configure(background='#e28743')
                profile1.showoriginal.grid(column= 4, row = i)
                profile1.showoriginal = Button(profile1,width=15, text = "Delete")
                profile1.showoriginal.configure(background='#e28743')
                profile1.showoriginal.grid(column= 5, row = i)
        i=i+1




if __name__ == '__main__':
    # test1.py executed as script
    # do something
    myprofile(id)
