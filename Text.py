from tkinter import *
import tkinter.scrolledtext as ScrolledText 
import os
from tkinter.filedialog import *	
def new():
    askopenfilename()
  
root=Tk()
root.title("Text Editor")
textArea=ScrolledText.ScrolledText(root,width=2000,height=1000)
text=Text(root,width=150,height=100)
text.grid()
menu=Menu(root)
root.config(menu=menu)
#for file in the menu bar 
fileMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="new",command=new)
fileMenu.add_command(label="open",command=new)
fileMenu.add_command(label="save",command=new)
fileMenu.add_command(label="save as",command=new)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=root.destroy)

#for open  in the menu bar
EditMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=EditMenu)
EditMenu.add_command(label="undo",command=new)
EditMenu.add_command(label="cut",command=new)
EditMenu.add_command(label="copy",command=new)
EditMenu.add_command(label="paste",command=new)
EditMenu.add_separator()
EditMenu.add_command(label="Exit",command=root.destroy)

#for view in the menu bar
ViewMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="view",menu=ViewMenu)
ViewMenu.add_command(label="status bar",command=new)
ViewMenu.add_command(label="hide menu",command=new)
ViewMenu.add_command(label="enter full screen",command=new)
ViewMenu.add_separator()
ViewMenu.add_command(label="Exit",command=root.destroy)

#for about in menu bar
aboutMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="about",menu=aboutMenu)
aboutMenu.add_command(label="help",command=new)
aboutMenu.add_separator()
aboutMenu.add_command(label="Exit",command=root.destroy)



root.mainloop()