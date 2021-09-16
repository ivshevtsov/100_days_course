

FULL_LIST=[]
FULL_DICT={}

n = int(input())

while n>0:
    line = input().split(';')
    if line[0] not in FULL_DICT:
        FULL_DICT[line[0]]=  [0, 0, 0, 0, 0] # all games[0]/wins[1]/equal[2]/lose[3]/all points[4]
    if line[2] not in FULL_DICT:
        FULL_DICT[line[2]] = [0, 0, 0, 0, 0]
    n-=1
    print(line)
    #all games
    FULL_DICT[line[0]][0] += 1
    FULL_DICT[line[2]][0] += 1
    #wins
    if int(line[1])>int(line[3]):
        #winner first team
        FULL_DICT[line[0]][1] += 1
        FULL_DICT[line[0]][4] += 3
        #loser
        FULL_DICT[line[2]][3] += 1

    elif int(line[1])<int(line[3]):
        #winner second team
        FULL_DICT[line[2]][1] += 1
        FULL_DICT[line[2]][4] += 3
        #loser
        FULL_DICT[line[0]][3] += 1

    elif int(line[1]) == int(line[3]):
        #first team
        FULL_DICT[line[0]][2] += 1
        FULL_DICT[line[0]][4] += 1
        #second team
        FULL_DICT[line[2]][2] += 1
        FULL_DICT[line[2]][4] += 1

for keys in FULL_DICT.keys():
    print(f'{keys}:', end='')
    print(*FULL_DICT[keys])
