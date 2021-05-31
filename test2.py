from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from fpdf import FPDF
root=Tk()
root.attributes("-fullscreen", False)
text = Text(root)
text.pack()

def view_image(*values):
    root = Toplevel()
    img = ImageTk.PhotoImage(file=values[0])
    image_label = ttk.Label(
        root,
        image=img,
        text='Images',
        compound='top'
    )
    image_label.pack()
#Insert Image

yourImage=filedialog.askopenfilenames(title = "Select your image",filetypes = [("Image Files","*.png"),("Image Files","*.jpg")])
#imgFile=Image.open(yourImage)
for i in yourImage:
    imgToInsert=ImageTk.PhotoImage(file=i)
    image_label = ttk.Label(
        text,
        image=imgToInsert,
        text='Python',
        compound='top'
    )
    image_label.pack()
# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# create a cell
pdf.cell(200, 10, txt = "GeeksforGeeks",
         ln = 1, align = 'C')

# add another cell
pdf.cell(200, 10, txt = "text",
         ln = 2, align = 'C')
for i in yourImage:
    pdf.image(name=i, x = None, y = None, w = 190, h = 100, type = '', link = '')

# save the pdf with name .pdf
pdf.output("GFG.pdf")
root.mainloop()









txt = scrolledtext.ScrolledText(noteview, undo=True)
txt['font'] = ('consolas', '12')
txt.pack(expand=True, fill='both')
if mycursor4:
    for images in mycursor4:
        for j in range(len(images)):
            if j==2:
                imgToInsert=ImageTk.PhotoImage(file=images[j])
                image_label = ttk.Label(
                    txt,
                    image=imgToInsert,
                    text='Python',
                    compound='top'
                )
                image_label.pack()
