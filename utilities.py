import settings

def height_percentage(percentage):
    return (settings.HEIGHT * percentage)/100
def width_percentage(percentage):
    return (settings.WIDTH * percentage)/100 
def mine_count():
    return (settings.GRID_SIZE**2)//4