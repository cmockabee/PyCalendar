# Cameron Mockabee 2017
# PyCalendar: Assignment Tracker and Urgency Identifier
# Add assignments and due dates.

from tkinter import *
from tkinter import ttk


#------------------------------------------
# Tarea Creation
#------------------------------------------

class Tarea:
   'Common base class for all employees'
   tareaCount = 0

   #assignment name, date due, and class code
   def __init__(self, name, datedue, code):
      self.name = name
      self.datedue = datedue
      tarea.tareaCount += 1
   

#------------------------------------------
# Menu Entry
#------------------------------------------
menuBool = True
master = Tk()
	   

while menuBool == True:   
	
	def menu():
		
		def show_entry_fields():
			   print("Assignment Name: %s\nDate Due: %s\nClass Code: %s" % (e1.get(), e2.get(), e3.get()))
			
		
		Label(master, text="Assignment Name").grid(row=0)
		Label(master, text="Date Due").grid(row=1)
		Label(master, text="Class Code").grid(row=2)

		e1 = Entry(master)
		e1.focus_set()
		e2 = Entry(master)
		e3 = Entry(master)

		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)
		e3.grid(row=2, column=1)


		btn2 = Button(master, text='Input Class', command=menu).grid(row=3, column=1, sticky=W, pady=4)
		btn1 = Button(master, text='Go To Schedule', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
	
	menu()
	
	menuBool = False

master.mainloop( )

   
   

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



#this will go in the menu function
tree.insert("" , 0,    text="Line 1", values=("1A","1b","1A","1b"))

id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B","1A","1b"))
##alternatively:
tree.insert("", 3, "dir3", text="Dir 3")
tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B","1A","1b"))

tree.pack()
root.mainloop()


