from tkinter import *
import settings
from utilities import * 

root = Tk()
# Override the Settings of the window
root.config(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title(settings.TITLE)

root.resizable(False, False)
# Frames
# Top Frame
top_frame= Frame(
    root, 
    bg="red",# Change later to black
    width=width_percentage(100),
    height=height_percentage(25)
    )
top_frame.place(x=0, y=0)
# Left Frame
left_frame= Frame(
    root, 
    bg="blue",# Change later to black
    width=width_percentage(25),
    height=height_percentage(75)
    )
left_frame.place(x=0, y=height_percentage(25))
# Run the window
root.mainloop()