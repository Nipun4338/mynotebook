from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from fpdf import FPDF
from datetime import datetime
timestamp = "2021-05-01 21:21:58"
date_time=datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
print(date_time)

print("Date time object:", date_time)

d = date_time.strftime("%d %B, %Y")
print("Output 2:", d)

d = date_time.strftime("%I:%M:%S %p")
print("Output 5:", d)
