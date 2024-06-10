from tkinter import Button
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None
    def create_cell_button(self, location):
        button = Button(
            location,
            width=12,
            height=6,
            text="button"
        )
        self.cell_button_object = button