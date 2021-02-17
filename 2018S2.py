import math
N = int(input())

matrix = []
for i in range(N):
    row = input().split()
    n = []
    for j in range(N):
        h = int(row[j])
        n.append(h)
    matrix.append(n)

four_end = [matrix[0][0],matrix[N-1][0],matrix[N-1][N-1],matrix[0][N-1]]
minimun = math.inf
pos = 4

for k in range(4):
    if four_end[k]<minimun:
       minimun = four_end[k]
       pos = k
       
def rotate_90_clockwise(mat):
    rotated = []
    for col in zip(*mat):
        rotated.append(list(reversed(col)))
    return rotated

def print_matrix(m):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in m]))
    
origin = matrix

if pos == 0:
    print_matrix(origin)
elif pos==1:
    print_matrix(rotate_90_clockwise(matrix))
elif pos==2:
    print_matrix(rotate_90_clockwise(rotate_90_clockwise(matrix)))
elif pos==3:
    print_matrix(rotate_90_clockwise(rotate_90_clockwise(rotate_90_clockwise(matrix))))

