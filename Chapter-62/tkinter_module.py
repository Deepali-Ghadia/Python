# Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python.
# create an instance of tk class and then pack all the widgets together

# widgets =>  Widget is an element of Graphical User Interface (GUI) that displays/illustrates information or gives a way for the user to interact with the OS.

# methods
# pack - to pack widgets
# grid - provides a grid like structure to place widgets
# place - places widget at a specific position

from tkinter import *

# It creates a basic GUI consisting of common components of all GUIs
object = Tk()

object.geometry("500x500") # widthxheight | specify the size of GUI window
object.minsize(100,100) #width,height
object.maxsize(900,900)

# label is a widget with which user does not interact => like text 
main_text = Label(text="Hello World!")
# to display the above text, you need to pack it
# geometry manager organizes widgets in blocks before placing them in the parent widget.

# adding image to GUI
photo = PhotoImage(file="Chapter-62/python_logo.png")
# Since user is not interacting with image, therefore we need to add it inside label
photo_label = Label(image = photo)
photo_label.pack() # first this will be shown
main_text.pack()





# called as eventloop and on execution a  GUI window is shown
object.mainloop() # makes GUI interactive and remembers the logic that you have implemented.

