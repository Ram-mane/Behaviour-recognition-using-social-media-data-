import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import cv2


root = tk.Tk()
root.title("Behaviour Types")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

frame_alpr = tk.LabelFrame(root, text=" ", width=500, height=600, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=100, y=10)


frame_alpr = tk.LabelFrame(root, text=" ", width=600, height=600, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=700, y=10)

l1 = tk.Label(root, text="1. ISTJ: Reliable and meticulous,ISTJs are known \n for their strong sense of duty and adherence to rules. ", font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=30)


l1 = tk.Label(root, text='2. ISFJ: Compassionate and nurturing, ISFJs are often the\n caring pillars of their communities. They have a keen eye\n for detail and are deeply committed to serving others.   ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=80)


l1 = tk.Label(root, text='3. INFJ: INFJs are insightful and empathetic individuals who\n possess a unique ability to understand and connect with \n others on a deep level.  ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=150)

l1 = tk.Label(root, text='4. INTJ: Independent and visionary, INTJs are highly analytical \n and strategic thinkers. They excel in complex problem-solving\n and have a natural inclination towards planning for the long-term.',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=220)

l1 = tk.Label(root, text='5. ISTP: ISTPs are hands-on problem solvers who thrive in practical,\n real-world situations. They have a natural curiosity and a \n knack for understanding how things work. ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=290)

l1 = tk.Label(root, text='6. ISFP: Gentle and artistic, ISFPs possess a deep appreciation for\n beauty and aesthetics. They have a strong sense of personal values ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=360)

l1 = tk.Label(root, text='7. INFP: INFPs are empathetic and creative individuals who prioritize\n authenticity and personal growth. ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=420)

l1 = tk.Label(root, text='8. INTP: INTPs are independent thinkers and problem solvers who \n love exploring theoretical concepts. They possess \n a natural curiosity and enjoy delving into complex ideas.',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=110, y=480)






l1 = tk.Label(root, text="9. ESTP: Energetic and action-oriented, ESTPs thrive fast-paced  environments. \n They are natural risk-takers who enjoy  pushing boundaries \n and seeking thrilling experiences. ", font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=30)


l1 = tk.Label(root, text='10. ESFP: ESFPs are outgoing and vivacious individuals who radiate positive energy.\n They enjoy being the center of attention and engaging with others.  ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=100)


l1 = tk.Label(root, text='11. ENFP: ENFPs are enthusiastic and passionate individuals who possess a natural \n ability to inspire others. They are creative and imaginative',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=150)

l1 = tk.Label(root, text='12. ENTP: Quick-witted and intellectually curious, ENTPs thrive in dynamic \n and challenging environments. ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=210)

l1 = tk.Label(root, text='13. ESTJ: Efficient and organized, ESTJs are natural leaders who value\n structure and order. They possess a strong work ethic and \n excel in managing projects and people. ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=270)

l1 = tk.Label(root, text='14. ESFJ: ESFJs are warm and caring individuals who prioritize the\n well-being of others. They are natural nurturers and \n often take on supportive roles within their communities. ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=340)

l1 = tk.Label(root, text='15.ENFJ: Charismatic and empathetic, ENFJs are natural leaders who excel\n in guiding and motivating others. ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=420)

l1 = tk.Label(root, text='16.ENTJ: Assertive and ambitious, ENTJs are born leaders who thrive in \n high-pressure environments. They are natural strategists and excel in \n implementing plans to achieve their goals. ',font=("Times new roman", 13), bg="#192841", fg="white")
l1.place(x=710, y=480)


root.mainloop()