import utilities
import random
import settings
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
        if self.is_mine:
            self.show_mines()
        else:
            self.show_mine_number()
    def get_mine_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell.is_mine
            
    def show_mine_number(self):
        count=0
        if(self.x-1>=0 and self.y-1>=0):
            count+=self.get_mine_by_axis(self.x-1, self.y-1)
        if(self.x-1>=0):
            count+=self.get_mine_by_axis(self.x-1, self.y)
        if(self.x-1>=0 and self.y+1<settings.GRID_SIZE):
            count+=self.get_mine_by_axis(self.x-1, self.y+1)
        if(self.y-1>=0):
            count+=self.get_mine_by_axis(self.x, self.y-1)
        if(self.y+1<settings.GRID_SIZE):
            count+=self.get_mine_by_axis(self.x, self.y+1)
        if(self.x+1<settings.GRID_SIZE and self.y-1>=0):
            count+=self.get_mine_by_axis(self.x+1, self.y-1)
        if(self.x+1<settings.GRID_SIZE):
            count+=self.get_mine_by_axis(self.x+1, self.y)
        if(self.x+1<settings.GRID_SIZE and self.y+1<settings.GRID_SIZE):
            count+=self.get_mine_by_axis(self.x+1, self.y+1)
        self.cell_button_object.configure(text=count)

    def show_mines(self):
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_button_object.configure(bg="red")
            else:
                cell.cell_button_object.configure(bg="black")
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