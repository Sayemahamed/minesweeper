import utilities
import random
import settings
from tkinter import Button
class Cell:
    all=[]
    cell_count=settings.GRID_SIZE**2 - utilities.mine_count()

    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x
        self.y = y
        self.is_visited=False

        #Append the object to the Cell class
        Cell.all.append(self)
    def create_cell_button(self, location):
        button = Button(
            location,
            width=12,
            height=4,
            text="x"
        )
        button.bind("<Button-1>",  self.left_click)
        button.bind("<Button-3>",  self.right_click)
        self.cell_button_object = button

    def left_click(self, event):
        if self.is_mine:
            self.show_mines()
        else:
            self.show_mine_number(self.x,self.y)
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    def show_mine_number(self,x,y):
        if self.get_cell_by_axis(x,y).is_visited:
            return
        self.get_cell_by_axis(x,y).is_visited=True
        Cell.cell_count-=1
        count=0
        if(x-1>=0 and y-1>=0):
            count+=self.get_cell_by_axis(x-1, y-1).is_mine
        if(x-1>=0):
            count+=self.get_cell_by_axis(x-1, y).is_mine
        if(x-1>=0 and y+1<settings.GRID_SIZE):
            count+=self.get_cell_by_axis(x-1, y+1).is_mine
        if(y-1>=0):
            count+=self.get_cell_by_axis(x, y-1).is_mine
        if(y+1<settings.GRID_SIZE):
            count+=self.get_cell_by_axis(x, y+1).is_mine
        if(x+1<settings.GRID_SIZE and y-1>=0):
            count+=self.get_cell_by_axis(x+1, y-1).is_mine
        if(x+1<settings.GRID_SIZE):
            count+=self.get_cell_by_axis(x+1, y).is_mine
        if(x+1<settings.GRID_SIZE and y+1<settings.GRID_SIZE):
            count+=self.get_cell_by_axis(x+1, y+1).is_mine
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                cell.cell_button_object.configure(text=count)
        if count==0:
            if(x-1>=0 and y-1>=0):
                self.show_mine_number(x-1, y-1)
            if(x-1>=0):
                self.show_mine_number(x-1, y)
            if(x-1>=0 and y+1<settings.GRID_SIZE):
                self.show_mine_number(x-1, y+1)
            if(y-1>=0):
                self.show_mine_number(x, y-1)
            if(y+1<settings.GRID_SIZE):
                self.show_mine_number(x, y+1)
            if(x+1<settings.GRID_SIZE and y-1>=0):
                self.show_mine_number(x+1, y-1)
            if(x+1<settings.GRID_SIZE):
                self.show_mine_number(x+1, y)
            if(x+1<settings.GRID_SIZE and y+1<settings.GRID_SIZE):
                self.show_mine_number(x+1, y+1)

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