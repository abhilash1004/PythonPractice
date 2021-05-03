from tkinter import *
# def hello(event):
# 	print('Single Click , Button-1')
# def quit(event):
# 	print('Double Click, so lets stop')
# 	import sys
# 	sys.exit()
# widget = Button(None,text='Mouse Clicks')
# #widget.pack()
# widget.bind('<Button-1>',hello)
# widget.bind('<Double-1>',quit)
# widget.grid(row=0,column=0)
# widget.mainloop()

def printName(n):
	print(n)

win = Tk()
win.geometry('500x650')
namelabel = Label(win,text='name').grid(row=0,column=0)

name = Entry(win)
name.grid(row=0,column=1)
printButton = Button(win,text='Print',command=lambda: printName(name.get())).grid(row=1,column=1)
mainloop()