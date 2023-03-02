#import libraies
import os
import pyglet
import convert_to_txt
import summarization as summary
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk
from tkinter import * 
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInput.get("1.0",'end-1c')
	convert_to_txt.clear()
	convert_to_txt.write(userInput)
	nn.delete("1.0","end")
	nn.insert("1.0", summary.summarization((convert_to_txt.read())))
	return userInput
# this is a function to clear text input box
def clear():
        convert_to_txt.clear() 
        tInput.delete("1.0","end")
        nn.delete("1.0","end")

# this is a function to get text from word file
def cpText(word=False):
	if(word): 
                file = askopenfilename(filetypes=[('word files', '*.docx')])
                if file is not None:                                       
                        filepath = os.path.abspath(file)
                        convert_to_txt.read_word_file(filepath)
                        tInput.delete("1.0","end")
                        tInput.insert("1.0", convert_to_txt.read())
                        nn.delete("1.0","end")
                        nn.insert("1.0", summary.summarization((convert_to_txt.read())))
	else:
	    file = askopenfilename(filetypes=[('text files', '*.txt')])
	    if file is not None:
                        filepath = os.path.abspath(file)
                        convert_to_txt.read(filepath)
                        tInput.delete("1.0","end")
                        tInput.insert("1.0", convert_to_txt.read())
                        nn.delete("1.0","end")
                        nn.insert("1.0", summary.summarization((convert_to_txt.read())))

    
root = Tk()
# add font file
pyglet.font.add_file('assets/fonts/CarterOne-Regular.ttf')
# add icon files
wordIcon = PhotoImage(file='assets/icons/word.png')
txtIcon = PhotoImage(file='assets/icons/txt.png')

# This is the section of code which creates the main window
root.geometry('650x500')
root.configure(background='#ffffff')
root.title('Text Summarization')

# This is the section of code which creates the a label
Label(root, text='input text',bg='#ffffff', fg='#fca311',
        font =("Carter One", 14)).place(x=14, y=13)


# This is the section of code which creates a text input box
tInput=scrolledtext.ScrolledText(root,height = 15, width = 60,bg='#14213d',
        fg='#fca311',padx = 15,pady=5)
tInput.place(x=14, y=50)


# This is the section of code which creates the a label

Label(root, text='output text',bg='#ffffff', fg='#fca311',font =("Carter One", 14)).place(x=14, y=308)

# This is the section of code which creates a text input box
nn=scrolledtext.ScrolledText(root,height = 6, width = 60,bg='#14213d', fg='#fca311',padx = 15,pady=5)
nn.place(x=14, y=345)


b1 = tk.Button(root, text = "Summarization",bg='#14213d', fg='#fca311',font =("Carter One", 10),width =12,command=getInputBoxValue)
b1.place(x=80, y=455)

b2 = tk.Button(root, text = "Clear",bg='#14213d', fg='#fca311',font =("Carter One", 10),width =6,command=clear)
b2.place(x=14, y=455)

b3 = tk.Button(root,image=wordIcon,text = "Word File",bg='#14213d', fg='#fca311',font =("Carter One", 10),width =80,height= 80,command=lambda: cpText(True))
b3.place(x=550, y=50)
b4 = tk.Button(root,image=txtIcon,text = "Word File",bg='#14213d', fg='#fca311',font =("Carter One", 10),width =80,height= 80,command=cpText)
b4.place(x=550, y=140)


root.mainloop()
