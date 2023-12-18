
from constant.settings import*

def cart_to_iso(x, y):
    iso_x = x - y
    iso_y = (x + y)/2
    return iso_x, iso_y

def get_cart_rect_pos (grid_x, grid_y):
    rect = [
        (grid_x * CELL_SIZE, grid_y * CELL_SIZE),
        (grid_x * CELL_SIZE + CELL_SIZE, grid_y * CELL_SIZE),
        (grid_x * CELL_SIZE + CELL_SIZE, grid_y * CELL_SIZE + CELL_SIZE),
        (grid_x * CELL_SIZE, grid_y * CELL_SIZE + CELL_SIZE)
    ]
    return rect

def get_iso_pos (grid_x, grid_y):
    return [cart_to_iso(x,y) for x,y in get_cart_rect_pos(grid_x, grid_y)]

def get_render_pos (grid_x, grid_y):
    iso_poly = get_iso_pos (grid_x, grid_y)
    min_x = min(vertex[0] for vertex in iso_poly)
    min_y = min(vertex[1] for vertex in iso_poly)
    return [min_x, min_y]
