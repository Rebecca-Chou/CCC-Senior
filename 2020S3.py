N = input()
H = input()

def get_his(n):
    his = [0]*26
    for letter in n:
        his[ord(letter)-97] += 1
    return his

def equ(f1, f2):
    for i in range(len(f1)):
        if f1[i]!=f2[i]:
            return False
    return True

histogram = get_his(N)
length = len(N)
num_sub = 0

sub = H[:length]
subs = {}
h = get_his(sub)
if equ(h,histogram):
    num_sub += 1
    subs[sub] = 1

for l in H[length:]:
    popout = sub[0]
    sub = sub[1:]+l
    h[ord(popout)-97] -= 1
    h[ord(l)-97] += 1
    if equ(h,histogram) and sub not in subs:
        num_sub += 1
        subs[sub] = 1

print(num_sub)
