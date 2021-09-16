
n = int(input())
x=0
y=0
while n>0:
    Word = input().split()
    if Word[0]=='запад':
        x=x-int(Word[1])
    elif Word[0]=='восток':
        x=x+int(Word[1])
    elif Word[0]=='север':
        y = y+int(Word[1])
    elif Word[0]=='юг':
        y = y-int(Word[1])
    n-=1
print(f'{x} {y}')