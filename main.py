from tkinter import *

root = Tk()
# Override the Settings of the window
root.config(bg="black")
root.geometry("1440x720")
root.title("MineSweeper")
root.resizable(False, False)
# Frame
top_frame= Frame(
    root, 
    bg="red",# Change later to black
    width=1440,
    height=180
    )
top_frame.place(x=0, y=0)

# Run the window
root.mainloop()