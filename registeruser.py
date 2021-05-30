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
        window1.minsize(800, 400)
        window1.maxsize(800, 400)
        Label(window1, text = "You have an active account!",font=('Impact', -20),bg='#456').grid(column= 0, row = 4)
    else:
        sql="Insert into profiles(phone) values('"+Ans+"')";
        mycursor1 = mydb.cursor()
        mycursor1.execute(sql)
        mydb.commit()
        first_face_dataset.takesample(Ans)


def regme():
    window= Tk()
    window.title('Register')
    window.minsize(800, 400)
    window.maxsize(800, 400)
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
    regme()
