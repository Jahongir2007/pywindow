'''
  Author: Jahongir Sobirov
  PyWindow python library
  Version: 1.1.0
  License: MIT
  All rights reserved
'''
import tkinter
from tkinter import *
def window(title, size, color):
    gui = Tk(className=title)

    gui.geometry(size)


    gui.configure(bg=color)

    gui.mainloop() 
def texteditor(fonttext, fontfamily, fontsize, fontstyle):
    root = tkinter.Tk()
    root.title(fonttext) 
      
    sample_text = tkinter.Text( root, height = 10)
    sample_text.pack()
      
    Font_tuple = (fontfamily, fontsize, fontstyle)
      
    sample_text.configure(font = Font_tuple)
    root.mainloop()
    
