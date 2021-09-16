len=4
F=0
j=0
mas = [[0]*len for i in range(len)]
list = [0]

for i in range(len**2):
    if F==0 and j>-(len-1):
        j -= 1
        list.append(j)
    elif j==-(len-1) and F==0:
        F=1
    if F==1 and j<len-1:
        j+=1
        list.append(j)
    elif F==1 and j==(len-1):
        F=0
        len=len-2
F=1
i=0
j=0
len=4
Val=0
for V in range(len**2-1):
    Val+=1
    if list[V]==0:
        F=(F+1)%2
        mas[i][j] = Val

    if list[V+1]<list[V] and F==0 and list[V]!=0:
        j += 1
        mas[i][j]=Val
    elif list[V+1]>list[V] and F==0 and list[V]!=0:
        i += 1
        mas[i][j] = Val
    elif list[V+1]>list[V] and F==1 and list[V]!=0:
        j-=1
        mas[i][j] = V
    elif list[V+1]<list[V] and F==1 and list[V]!=0:
        i -= 1
        mas[i][j] = Val



print(mas)
print(list)