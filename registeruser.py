from tkinter import *
import first_face_dataset, registeruser, second_face_training
import mysql.connector


#call to start video to capture images, parameter=id
def video(Ans):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="mynotebook"
    )

    mycursor = mydb.cursor()
    sql="SELECT * FROM profiles where phone='"+Ans+"'";
    mycursor.execute(sql)

    myresult = mycursor.fetchone()
    if(myresult):
        window1= Tk()
        window1.title('Alert')
        window1.minsize(300, 50)
        window1.maxsize(300, 50)
        window1.configure(background='#456')
        Label(window1, text = "You have an active account!",font=('Impact', -20),bg='#456',fg="#df4759").place(relx = 0.5,
                           rely = 0.5,
                           anchor = 'center')
    else:
        sql="Insert into profiles(phone) values('"+Ans+"')";
        mycursor1 = mydb.cursor()
        mycursor1.execute(sql)
        mydb.commit()
        first_face_dataset.takesample(Ans)


def regme():
    window= Tk()
    window.title('Register')
    window.minsize(600, 50)
    window.maxsize(600, 50)
    Label(window, text = "Enter Only Your Decimal Phone Number for Register:",font=('Impact', -15),borderwidth=1, relief="sunken", fg='#000').grid(column= 0, row = 4, padx = 10, pady = 10)
    num1 = Entry(window,width=20)
    num1.grid(column= 1, row = 4)
    Ans = str(num1.get())
    window.video = Button(window, text = "Take video training",font=('Impact', -12),fg='#fff',command = lambda:[video(str(num1.get()))])
    window.video.configure(background='#e28743')
    window.video.grid(column= 2, row = 4)
    #first_face_dataset.takesample(Ans)


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    regme()
