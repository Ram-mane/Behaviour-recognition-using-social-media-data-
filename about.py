import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import cv2


window = tk.Tk()
window.geometry("800x800")
window.title("About Us")
window.configure(background="white")

l1 = tk.Label(window, text="Behaviour Recognition Using Social Media Post", font=("Times new roman", 20, "bold"), bg="#192841", fg="white")
l1.place(x=120, y=30)


l1 = tk.Label(window, text="BE FINAL YEAR PROJECT \n Student Modern Education Society College Of Engineering Pune \n Department Of Computer Science & Engineering", font=("Times new roman", 15, "bold"), bg="white", fg="black")

l1.place(x=150, y=100)


img = Image.open('about1.png')
img = img.resize((500,300), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(window, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=150, y=250)




window.mainloop()