#input
line = input().split()
N = int(line[0])
M = int(line[1])

grid = []
emptyCells = {}
processed = set()
for i in range(N):
    row = []
    line = input()
    for j in range(M):
        cell = line[j]
        row.append(cell)
        if cell=='S':
            startCell = (i,j)
        elif cell=='.':
            emptyCells[(i,j)] = -1
    grid.append(row)

#calculate
def camara_pass(c):
    if c=='.' or c=='L' or c=='R' or c=='U' or c=='D':
        return True
    return False

def isUnderCamera(i,j):
    if grid[i][j]=='C':
        return True
    if grid[i][j]=='.' or grid[i][j]=='S':
        x=1
        while camara_pass(grid[i-x][j]):
            x += 1
        if grid[i-x][j]=='C':
            return True
        x=1
        while camara_pass(grid[i+x][j]):
            x += 1
        if grid[i+x][j]=='C':
            return True
        x=1
        while camara_pass(grid[i][j-x]):
            x += 1
        if grid[i][j-x]=='C':
            return True
        x=1
        while camara_pass(grid[i][j+x]):
            x += 1
        if grid[i][j+x]=='C':
            return True
    return False

def checkCells(old_cells, new_cells, step):
    sameStep = []
    while len(old_cells)>0:
        for old_cell in old_cells:
            if old_cell in processed:
                continue
            else:
                processed.add(old_cell)
            i = old_cell[0]
            j = old_cell[1]

            if grid[i][j]=='W':
                continue
                
            if grid[i][j]=='.' or grid[i][j]=='S':
                if not isUnderCamera(i,j):
                    if grid[i][j]=='.':
                        emptyCells[(i,j)] = step
                    #up
                    if i>0 and (i-1,j) not in processed:
                        new_cells.append((i-1,j))
                    #down
                    if i<N-1 and (i+1,j) not in processed:
                        new_cells.append((i+1,j))
                    #left
                    if j>0 and (i,j-1) not in processed:
                        new_cells.append((i,j-1))
                    #right
                    if j<M-1 and (i,j+1) not in processed:
                        new_cells.append((i,j+1))
                        
            elif grid[i][j]=='L'and j>0 and (i,j-1) not in processed:
                    sameStep.append((i,j-1))
                    
            elif grid[i][j]=='D'and i<N-1 and (i+1,j) not in processed:
                    sameStep.append((i+1,j))
                    
            elif grid[i][j]=='R'and j<M-1 and (i,j+1) not in processed:
                    sameStep.append((i,j+1))
                    
            elif grid[i][j]=='U'and i>0 and (i-1,j) not in processed:
                    sameStep.append((i-1,j))

        old_cells = sameStep
        sameStep = []
                        

def get_steps(start, step):
    old_cells = []
    new_cells = [start]
    while len(new_cells)>0:
        old_cells = new_cells
        new_cells = []
        checkCells(old_cells,new_cells,step)
        step += 1

step = 0
get_steps(startCell, step)



#output
for key, value in emptyCells.items():
    print(value)
