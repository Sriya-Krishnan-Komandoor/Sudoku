from random import sample
from selection import SelectNumber
from copy import deepcopy



def create_line_coordinates(cell_size:int) -> list[list[tuple]]:
    """Creates the y,y coordinates for drawing the grid lines"""
    points = []
    for y in range(1,9):
        #horizontal lines
        temp = []
        temp.append((0, y * cell_size)) #x,y points [(0,100),(0,200),(0,300)...]
        temp.append((900, y * cell_size))#x,y points [(900,100),(900,200),(900,300)...]
        points.append(temp)
    for x in range(1,10):#10 to close the grid lines on the right
        temp = []
        temp.append((x * cell_size,0))
        temp.append((x*cell_size,900))
        points.append(temp)
    #print(points)
    return points

SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE


def pattern(row_num: int, col_num: int) -> int:
    return (SUB_GRID_SIZE*(row_num % SUB_GRID_SIZE) + row_num // SUB_GRID_SIZE +col_num)%GRID_SIZE


def shuffle(samp: range) -> list:
    return sample(samp,len(samp))

def create_grid(sub_grid: int) ->list[list]:
    """Create the 9x9 grid filled with random numbers"""
    row_base=range(sub_grid)
    rows=[g * sub_grid + r for g in shuffle(row_base) for r in shuffle(row_base)]
    cols = [g * sub_grid + c for g in shuffle(row_base) for c in shuffle(row_base)]
    nums=shuffle(range(1, sub_grid * sub_grid +1))
    return [[nums[pattern(r,c)] for c in cols]for r in rows]

def remove_numbers(grid:list[list]) ->None:
    """get zeros on the grid"""
    num_of_cells=GRID_SIZE*GRID_SIZE
    empties=num_of_cells * 3 // 7 # lower the num-harder the game
    for i in sample(range(num_of_cells),empties):
        grid[i // GRID_SIZE][i % GRID_SIZE]=0


class Grid:
    def __init__(self, pygame, font):
        self.cell_size = 100
        self.line_coordinates=create_line_coordinates(self.cell_size)
        self.num_x_offset=35
        self.num_y_offset=12
        self.grid = create_grid(SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid) # creates copy before removing numbers
        self.win = False


        remove_numbers(self.grid)
        self.occupied_cell_coordinates = self.pre_occupied_cells()
        #print(self.pre_occupied_cells())
        self.game_font = font
        self.selection = SelectNumber(pygame, self.game_font)

    def restart(self)-> None:
        self.grid = create_grid(SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)
        remove_numbers(self.grid)
        self.occupied_cell_coordinates = self.pre_occupied_cells()
        self.win = False


    def check_grids(self):
        '''checks if all the cells in the main grid and the test grid are equal'''
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != self.__test_grid[y][x]:
                    '''here'''
                    return False
            return True


    def is_cell_preoccupied(self, x: int, y: int) -> bool:
        """check for cells that are initialized"""
        for cell in self.occupied_cell_coordinates:
            if x == cell[1] and y == cell[0]: # x is col and y is row
                return True
        return False



    def get_mouse_click(self, x: int, y: int) -> None:
        if x <=900:
            grid_x, grid_y = x // 100, y // 100
            #print(grid_x, grid_y) mouse position on the grid
            if not self.is_cell_preoccupied(grid_x, grid_y):
                self.set_cell(grid_x, grid_y, self.selection.selected_number)
        self.selection.button_clicked(x, y)
        if self.check_grids():
            print("Won, Game Over!")
            self.win = True




    def pre_occupied_cells(self) -> list[tuple]:
        """Gather the y,x coordinates for all preoccupied/initialised cells"""
        occupied_cell_coordinates = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x, y) != 0:
                    occupied_cell_coordinates.append((y,x)) #first row, then column
        return occupied_cell_coordinates

    def __draw_lines(self,pg,surface)->None:
        for index,point in enumerate(self.line_coordinates):
            if index == 2 or index == 5 or index == 10 or index == 13:
                pg.draw.line(surface, (255, 200, 0), point[0], point[1])

            else:
                pg.draw.line(surface, (0, 50, 0), point[0], point[1])
    def show(self):
        for cell in self.grid:
            print(cell)

    def __draw_numbers(self, surface) -> None:
        """draw the grid numbers"""
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x,y)!=0:
                    if (y, x) in self.occupied_cell_coordinates:
                        text_surface = self.game_font.render(str(self.get_cell(x,y)),False,(0, 200, 255))
                    else:
                        '''here'''
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (0, 255, 0))

                    if self.get_cell(x, y) != self.__test_grid[y][x]:
                        '''here'''
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (255, 0, 0))
                        '''can we add a count here maybe'''

                    surface.blit(text_surface, (x * self.cell_size + self.num_x_offset, y * self.cell_size + self.num_y_offset))

    def draw_all(self,pg,surface):
        self.__draw_lines(pg,surface)
        self.__draw_numbers(surface)
        self.selection.draw(pg, surface)

    def get_cell(self, x: int,y: int )->int:
        """get a cell value at y,x coordinate"""
        return self.grid[y][x]

    def set_cell(self, x: int,y: int, value: int )->None:
        """set a cell value at y,x coordinate"""
        self.grid[y][x]= value



if __name__ == "__main__":
    grid = Grid()
    grid.show()

