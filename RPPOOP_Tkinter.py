#!/usr/bin/env python
# coding: utf-8

# In[104]:


#import tkinter as tk
from tkinter import *

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

m = tk.Tk()
m.title("Club Management System")
m.geometry("500x1000")

canvas = tk.Canvas(m, height=700, width=1400)
canvas.pack(side=tk.TOP)

scrollbar = tk.Scrollbar(m, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

label1 = tk.Label(frame, text='College of Engineering, Pune',background = "yellow" ,width=70, height = 1, font = ('Aerial', 25))
label1.pack()
label2 = tk.Label(frame, text='Clubs :',font = ('Aerial', 23) ,justify = LEFT)
label2.pack(pady=10, side= TOP, anchor = "w")
label3=tk.Label(frame, text='The various clubs of CoEP provide the students the much-cherished opportunity to come together to discuss and exchange ideas with like-minded people.\nHere, there’s something for everyone!', font=('Aerial', 15), justify = LEFT)
label3.pack(pady = 10, side = TOP, anchor = "w")
label4=tk.Label(frame, text='These are our Clubs: \n\nAarya Raas\nAbhijaat Newsletter\nArts and Crafts\nAstronomy Club\nBHAU’s Innovation & Entrepreneurship Cell\nBoat Club\nBoat Club Quiz Club\nCivil Services Aspirants Club\nCOEP ACM\nCOEP Consulting Club\nCOEP CSI Student Chapter\nCOEP Philomystics\nCoFSUG\nCultural Club\nDebate Club\nHAM Club\nHistory Club\nIgnited Innovators of India\nInformation and Cyber Security Research Group\nJaneev Club\nPersonality Development club\nRamanujan Mathematics Club\nRobot Study Circle\nSatellite Team\nScience Club\nSociety of Women Engineers\nSoftware Developement Section\nSpandan\nSpic Macay\nAbhiyanta', font=('Aerial', 15), justify = LEFT)
label4.pack(pady = 10, side = TOP, anchor = "w")



m.mainloop()


# In[ ]:





# In[ ]:




