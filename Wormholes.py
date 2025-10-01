"""
NAME: methind1
PROB: wormhole
LANG: PYTHON3
"""

pairings = []
iterations = 0

def pair(N, node, iterations, selected = [], current_set = []):
    new_pair = []
    for i in range(node+1, N):
        if i not in selected and i != node:
            new_pair = [node, i]
            if len(current_set) == N // 2 - 1:
                pairings.append(current_set + [new_pair])

            for k in range(N):
                iterations += 1
                if k not in selected and k != i and k != node:
                    pair(N, k, iterations, selected+[node, i], current_set + [new_pair])
                    break

def same_y(N, positions, iterations):
    ymap = [-1 for i in range(N)]
    x = 0
    y = 1
    i = 0
    for pos1 in positions:
        k = 0
        minx = 1000000000

        for pos2 in positions:
            iterations += 1
            if i != k:
                if pos1[y] == pos2[y]:
                    if pos1[x] < pos2[x]:
                        if pos2[x] - pos1[x] < minx:
                            minx = pos2[x] - pos1[x]
                            ymap[i] = k

            k += 1

        i += 1

    return ymap
                        

def check(spawn: int, config: list, yMap: list, iterations):
    escapable = True
    current_location = spawn

    while escapable:
        iterations += 1
        if yMap[current_location] == -1:
            break

        current_location = config[yMap[current_location]]

        if current_location == spawn:
            escapable = False

    return escapable
            
def format(N, config, iterations):
    ret = []
    for case in config:
        new_list = [0 for i in range(N)]

        for arr in case:
            new_list[arr[0]] = arr[1]
            new_list[arr[1]] = arr[0]
            iterations += 1

        ret.append(new_list)

    return ret
    

answer = 0

fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')

N = int(fin.readline())
positions = []
pair(N, 0, iterations)
arrangements = pairings

for i in range(N):
    pos = list(map(int, fin.readline().split()))
    positions.append(pos)

arrangements = format(N, arrangements, iterations)
yMap = same_y(N, positions, iterations)


for arrangement in arrangements:
    
    trappable = False

    for i in range(N):
        pos_i_escapable = check(i, arrangement, yMap, iterations)

        if not pos_i_escapable:
            trappable = True

        iterations += 1

    if trappable:
        answer += 1

fout.write('%d\n' % (answer))
