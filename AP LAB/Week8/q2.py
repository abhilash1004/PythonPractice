from tkinter import *
class Calculator(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
		self.numbers=[]
	def createWidgets(self):
		self.answer = Label(self,text='ans: ')
		self.answer.grid(row=0,column=0)
		
		self.button1=Button(self,text='1',command=lambda: self.updateEquation(1))
		self.button1.grid(row=1,column=0)
		#self.button1.bind('<Button-1>',self.updateEquation(1))

		self.button2=Button(self,text='2',command=lambda: self.updateEquation(2))
		self.button2.grid(row=1,column=1)

		self.button3=Button(self,text='3',command=lambda: self.updateEquation(3))
		self.button3.grid(row=1,column=2)

		self.button4=Button(self,text='4',command=lambda: self.updateEquation(4))
		self.button4.grid(row=2,column=0)

		self.button5=Button(self,text='5',command=lambda: self.updateEquation(5))
		self.button5.grid(row=2,column=1)

		self.button6=Button(self,text='6',command=lambda: self.updateEquation(6))
		self.button6.grid(row=2,column=2)

		self.button7=Button(self,text='7',command=lambda: self.updateEquation(7))
		self.button7.grid(row=3,column=0)

		self.button8=Button(self,text='8',command=lambda: self.updateEquation(8))
		self.button8.grid(row=3,column=1)

		self.button9=Button(self,text='9',command=lambda: self.updateEquation(9))
		self.button9.grid(row=3,column=2)

		self.button10=Button(self,text='0',command=lambda: self.updateEquation(0))
		self.button10.grid(row=4,column=0)

		self.button11=Button(self,text='+',command=lambda: self.updateEquation('+'))
		self.button11.grid(row=1,column=4)

		self.button12=Button(self,text='-',command=lambda: self.updateEquation('-'))
		self.button12.grid(row=2,column=4)

		self.button13=Button(self,text='*',command=lambda: self.updateEquation('*'))
		self.button13.grid(row=3,column=4)

		self.button14=Button(self,text='/',command=lambda: self.updateEquation('/'))
		self.button14.grid(row=4,column=4)

		self.button14=Button(self,text='=',command=self.solveEquation)
		self.button14.grid(row=4,column=3)

		self.button15=Button(self,text='clr',command=self.clearEquation)
		self.button15.grid(row=4,column=1)

	def clearEquation(self):
		del self.numbers[0:3]
		self.answer.configure(text="Enter numbers")

	def updateEquation(self,a):
		#str = a
		flag1=['+','-','*','/']
		flag2 = [i for i in range(10)]
		if len(self.numbers)==0 and a in flag2:
			self.numbers.append(a)
			self.answer.configure(text=str(a))
		elif len(self.numbers)==1:
			if a in flag1:
				self.numbers.append(a)
				self.answer.configure(text=str(self.numbers[0])+str(self.numbers[1]))
			else:
				self.numbers[0] = int(str(self.numbers[0])+str(a))
				self.answer.configure(text=str(self.numbers[0]))
		elif len(self.numbers)==2 and a in flag2:
			self.numbers.append(a)
			self.answer.configure(text=str(self.numbers[0])+str(self.numbers[1])+str(self.numbers[2]))
		elif len(self.numbers)==3:
			if a in flag2:
				self.numbers[2] = int(str(self.numbers[2])+str(a))
				self.answer.configure(text=str(self.numbers[0])+str(self.numbers[1])+str(self.numbers[2]))

	def solveEquation(self):
		val = 0
		if len(self.numbers)!=3:
			return
		if self.numbers[1] == '+':
			val = self.numbers[0] + self.numbers[2]
		elif self.numbers[1] == '-':
			val = self.numbers[0] - self.numbers[2]
		elif self.numbers[1] == '*':
			val = self.numbers[0] * self.numbers[2]
		elif self.numbers[1] == '/':
			val = self.numbers[0] / self.numbers[2]
		self.answer.configure(text=str(self.numbers[0])+str(self.numbers[1])+str(self.numbers[2])+"="+str(val))


c = Calculator()
mainloop()

