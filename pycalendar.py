# Cameron Mockabee 2017
# PyCalendar: Assignment Tracker and Urgency Identifier
# Add assignments and due dates.

from tkinter import *
from tkinter import ttk
import datetime


today = datetime.date.today()
closestSunday = datetime.timedelta(days=(datetime.date.today().weekday() + 1))
closestSundayDate = today - closestSunday
print('Closest Sunday	:', closestSundayDate)
print ('Today    :', today)

one_week = datetime.timedelta(days=7)


#------------------------------------------
# Tarea Creation
#------------------------------------------

tareaList = []

class Tarea:
   'Common base class for all employees'
   tareaCount = 0

   #assignment name, date due, and class code
   def __init__(self, name, datedue, code):
      self.name = name
      self.datedue = datedue
      Tarea.tareaCount += 1
   

#------------------------------------------
# Tree Framework
#------------------------------------------

root = Tk()
tree = ttk.Treeview(root)

tree["columns"]=("one","two","three","four")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.column("three", width=100 )
tree.column("four", width=100)
tree.heading("one", text="Date Due")
tree.heading("two", text="Class")
tree.heading("three", text="Assignment")
tree.heading("four", text="extra")

# This creates 6 week view starting from closest past Sunday
for x in range (1, 9):
	tree.insert("", 0, closestSundayDate, text=closestSundayDate)
	tree.insert(closestSundayDate, 0, text="Date Due",values=("x", "x","x","x"))
	closestSundayDate += one_week
	
tree.pack()



#------------------------------------------
# Menu Entry
#------------------------------------------
menuBool = True
master = Tk()  

while menuBool == True:   
	
	def menu():		
		
		def insert_assignment():
			assignmentDate = datetime.datetime.strptime(e2.get(), "%Y-%m-%d").date()
			closestSundayTarea = assignmentDate - (datetime.timedelta(days= (assignmentDate.weekday() + 1)))
			
			tree.insert(closestSundayTarea, 0, text=assignmentDate,values=(e1.get(), e2.get(),e3.get(),"1b"))
			obj = Tarea(e1.get(),e2.get(),e3.get())
			tareaList.append(obj)
			menu()
		
		
		Label(master, text="Assignment Name").grid(row=0)
		Label(master, text="Date Due").grid(row=1)
		Label(master, text="Class Code").grid(row=2)
		
		# Inputs
		e1 = Entry(master)
		e1.focus_set()
		e2 = Entry(master)
		e3 = Entry(master)

		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)
		e3.grid(row=2, column=1)

		# Quit Program Button
		# Insert Assignment Button
		btn1 = Button(master, text='Quit', command=quit).grid(row=3, column=0, sticky=W, pady=4)
		btn2 = Button(master, text='Insert Class', command=insert_assignment).grid(row=3, column=1, sticky=W, pady=4)	
	
	menu()
	
	menuBool = False

master.mainloop( )  

root.mainloop()


