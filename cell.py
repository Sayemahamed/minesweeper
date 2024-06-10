import utilities
import random
from tkinter import Button
class Cell:
    all=[]
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x
        self.y = y

        #Append the object to the Cell class
        Cell.all.append(self)
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
    # Self Printing

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    @staticmethod
    def randomize_mines():
        selected_cells=random.sample(Cell.all, utilities.mine_count())
        for cell in selected_cells:
            cell.is_mine=True