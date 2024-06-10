from tkinter import Button
class Cell:
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x
        self.y = y
    def create_cell_button(self, location):
        button = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        button.bind("<Button-1>",  self.left_click)
        button.bind("<Button-3>",  self.right_click)
        self.cell_button_object = button

    def left_click(self, event):
        print(event)
        print("left")

    def right_click(self, event):
        print(event)
        print("right")