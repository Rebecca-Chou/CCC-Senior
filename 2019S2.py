import math
T = int(input())
num = []

def is_prime(n):
    if n > 1:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if (n % i) == 0:
                return False
        return True
    return False

for i in range(T):
    line = int(input())
    s = 2*line
    for j in range(2,line+1):
        if is_prime(j)==False:
            continue
        else:
            com = s-j
            if is_prime(com):
                pair = [str(j),str(com)]
                num.append(pair)
                break

for l in num:
    print(' '.join(l))



            
    
