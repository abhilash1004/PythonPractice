from tkinter import *
# import sys 
# win = Tk()
# win.columnconfigure(0,weight=1)
# win.rowconfigure(0,weight=8)
# b1 = Button(win,text='GoodBye',command=sys.exit)
# #b1.pack()
# label = Label(win,text="Hello",background='White',foreground='red',font='Times 20',relief='groove',borderwidth=3)
# label.grid(row=0,column=0)
# b1.grid(row=1,column=1)
# text = Text(win)
# text.grid(row=0,column=0,sticky='nesw')
# vertical_scroller = Scrollbar(win,orient='vertical')
# vertical_scroller.grid(row=0,column=1,sticky='ns')
# horizontal_scroller = Scrollbar(win,orient='horizontal')
#horizontal_scroller.grid(row=1,column=0,sticky='ew')
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
		self.count_value = 0
	def create_widgets(self):
		self.count_label = Label(self,text="Count=0")
		self.count_label.grid(row=0,column=1)
		self.incr_button=Button(self,text="Increment",command=self.increment_count)
		self.incr_button.grid(row=0,column=0)
		self.quit_button = Button(self,text="Quit",command=self.master.destroy)
		self.quit_button.grid(row=1,column=0)
	def increment_count(self):
		self.count_value+=1
		self.count_label.configure(text="Count:"+str(self.count_value))
app = Application()
mainloop()
