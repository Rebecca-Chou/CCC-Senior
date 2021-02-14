sequence = input()
frequency = {'H':0, 'V':0}

for letter in sequence:
    if letter == 'H':
        frequency['H'] += 1
    elif letter == 'V':
        frequency['V'] += 1

num_h = frequency['H']%2
num_v = frequency['V']%2

grid = [['1','2'],['3','4']]

if num_h==1:
    tem = grid[0]
    grid[0] = grid[1]
    grid[1] = tem

if num_v==1:
    tem1 = grid[0][0]
    tem2 = grid[1][0]
    grid[0][0] = grid[0][1]
    grid[1][0] = grid[1][1]
    grid[0][1] = tem1
    grid[1][1] = tem2

for l in grid:
    print(' '.join(l))
