import numpy as np

grid = np.array([[c for c in line.strip('\n')] for line in open('testinput')])
                    
class RadialGrid:
    def __init__(self,cartesian_grid,origin):
        self.cartesian_grid = cartesian_grid
        self.origin = origin
        
    def radial_return(self,r,cardinal):
        og_row = self.origin[0]
        og_col = self.origin[1]
        
        if cardinal == 0: #east
            return self.cartesian_grid[og_row][og_col+r]
        elif cardinal == 1: #northeast
            return self.cartesian_grid[og_row-r][og_col+r]
        elif cardinal == 2: #north
            return self.cartesian_grid[og_row-r][og_col]
        elif cardinal == 3: #northwest
            return self.cartesian_grid[og_row-r][og_row-r]
        elif cardinal == 4: #west
            return self.cartesian_grid[og_row][og_col-r]
        elif cardinal == 5: #southwest
            return self.cartesian_grid[og_row+r][og_col-r]
        elif cardinal == 6: #south
            return self.cartesian_grid[og_row+r][og_col]
        elif cardinal == 7: #southeast
            return self.cartesian_grid[og_row+r][og_col+r]            
        else:
            return Exception('Bad input')
        
a = RadialGrid(grid[0:4,0:4],(0,0))