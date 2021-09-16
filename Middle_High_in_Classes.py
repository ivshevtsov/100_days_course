SUM={}
N = {}
with open('C:/Users/SH/Downloads/dataset_3380_5.txt') as Words:
    for line in Words:
        String = line.strip().split()
        if (String[0]) not in SUM:
            SUM[String[0]]=0
            SUM[String[0]]=SUM[String[0]]+int(String[2])
        else:
            SUM[String[0]] = SUM[String[0]] + int(String[2])
        if String[0] not in N:
            N[String[0]] = 0
            N[String[0]] += 1
        else:
            N[String[0]] += 1
print(SUM)
print(N)
for i in range(11):
    if str(i+1) in SUM:
        MIDDLE = SUM[str(i+1)]/N[str(i+1)]
        print(f'{i+1} {MIDDLE}')
    else:
        print(f'{i + 1} -')
