Py Calendar

This is a Python 3.6.3 applet that allows the user to keep track of their upcoming assignments.

When running PyCalendar.py, a tkinter tree view is created that has nodes for each Sunday for 6 weeks, starting with the Sunday of the current week. Each week begins with Sunday (index day 0) and ends with Saturday (index day 6).

Using the entry window, the user inputs the assignment, the due date in "YYYY-MM-DD" format, the class code, and clicks input.

This places the assignment into the tree under the node for the week that the assignment is due. If the assignment is due on a Sunday, it is placed under the prior week's node so that is visible ahead of time.

Upon close, the information is serialized using Pickle. Later initializations will retrieve this info and auto-restore the tree.

To-Do:
- Delete assignments
- Different colored rows for homework, quizzes, or exams
- Sorting by column
