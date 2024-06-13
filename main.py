from tkinter import *
from cell import Cell
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
    bg="black",
    width=width_percentage(100),
    height=height_percentage(25)
    )
top_frame.place(x=0, y=0)
label =Label(
    top_frame,
    text="Minesweeper Game",
    bg="black",
    fg="white",
    font=("", 40)
)
label.place(x=width_percentage(25), y=0)
# Left Frame
left_frame= Frame(
    root, 
    bg="black",
    width=width_percentage(25),
    height=height_percentage(75)
    )
left_frame.place(x=0, y=height_percentage(25))
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
# Center Frame
center_frame= Frame(
    root, 
    bg="blue",
    width=width_percentage(75),
    height=height_percentage(75)
    )
center_frame.place(x=width_percentage(25), y=height_percentage(25))
# Button 
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_cell_button(center_frame)
        c.cell_button_object.grid(row = x,column=y)
Cell.randomize_mines()
# for cell in Cell.all: 
#     print(cell.is_mine)
# Run the window 
root.mainloop() 
