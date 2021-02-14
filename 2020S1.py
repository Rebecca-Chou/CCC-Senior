N = int(input())
observations = []

for i in range(N):
    observation = []
    line = input().split()
    observation.append(int(line[0]))
    observation.append(int(line[1]))
    observations.append(observation)

def get_time(ele):
    return ele[0]

observations.sort(key=get_time)
pre_time = None
pre_pos = None
max_speed = -1

for obs in observations:
    time = obs[0]
    pos = obs[1]

    if pre_time == None and pre_pos == None:
        pre_time = time
        pre_pos = pos
        continue

    speed = abs(pos-pre_pos)/(time-pre_time)
    max_speed = max(max_speed,speed)

    pre_time = time
    pre_pos = pos

print(max_speed)


    
