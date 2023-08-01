from time import *
from tkinter import *

root =Tk()
root.title("Digital clock")
root.geometry("420x150")
root.configure(background ="black")
root.resizable(0,0)

def start():
	text =strftime("%H:%M:%S:%p")
	lable.config(text =text)
	lable.after(2000,start)

lable =Label(root,font =("ds-digital",50,"bold"),bg="black",fg ="red",bd=50)
lable.grid(row=0,column=1)
lable.pack(anchor ='center')
start()
print("done")
root.mainloop()