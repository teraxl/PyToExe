# -*- coding: utf-8 -*-
'''
Created on 26 february 2018 year.
@author: Aleksandr.Muga
'''
from tkinter import *

root = Tk()

def Hello(event):
    print("Yet now anather hello world")
    
btn = Button(root,
             text = "Click Me",
             width = 30,
             height = 5,
             bg = "white", fg = "black")
btn.bind("<Button - 1>", Hello)
btn.pack()
root.mainloop()
