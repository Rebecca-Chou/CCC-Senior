import sys

#read the input
M = int(input())
N = int(input())
room = []

for r in range(M+1):
    if r==0:
        room.append([0]*(N+1))
    else:
        line = input().split()
        room.append([0]+[int(i) for i in line])

target = M*N
path_value = []
val = room[1][1]
path_value.append(val)
cur_pos = 0

if val==target:
    print("yes")
    sys.exit()

while cur_pos<len(path_value):
    #find all the possible next step from one cell
    for i in range(1,M+1):
        p_val = path_value[cur_pos]
        if p_val % i!=0:
            continue
        for j in range(1,N+1):
            if p_val == i*j:
                val = room[i][j]
                if val==target:
                    print("yes")
                    sys.exit()
                if val not in path_value:
                    path_value.append(room[i][j])
    cur_pos += 1
print("no")
