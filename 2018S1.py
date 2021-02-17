import math
N = int(input())
villages = []

for i in range(N):
    n = int(input())
    villages.append(n)

villages.sort()
min_neigh = math.inf
now = villages[1]
pre = villages[0]

for v in villages[2:]:
    nex = v
    neigh_size = (now-pre)/2 + (nex-now)/2
    min_neigh = min(neigh_size,min_neigh)
    pre = now
    now = nex

print("{:.1f}".format(min_neigh))
    
    
    
