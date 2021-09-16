class User:
    'Class for all users'
    user_count=0
    def __init__(self, name , age , adress ):
        self.name = name
        self.age = age
        self.adress = adress

    def User_param(self):
        print(f'{self.name} from {self.adress}')

USER_1 = User('Ivan', 22, 'Rostov')
USER_1.User_param()

File = open('C:/Users/SH/Downloads/dataset.txt')
Word=File.readline()
print(Word)
STRING=''
for i in range(len(Word)):
    if Word[i].isalpha():
        if Word[i+1].isnumeric() and Word[i+2].isnumeric():
            Num=int(Word[i+1]+Word[i+2])
        elif Word[i+1].isnumeric():
            Num = int(Word[i + 1])
    while Num>0:
        STRING = STRING+Word[i]
        Num-=1

#print(STRING)
FULL=''
FULL_LIST=[]
FULL_DICT={}
with open('C:/Users/SH/Downloads/dataset_3363_3.txt') as Words:
    for line in Words:
        FULL=FULL+line
FULL_LIST=FULL.lower().split()
FULL_SET=set(FULL_LIST)
for Word in FULL_LIST:
    if Word in FULL_SET and Word in FULL_DICT:
        FULL_DICT[Word]+=1
    elif Word in FULL_SET and Word not in FULL_DICT:
        FULL_DICT[Word] = 1
MAX=max(FULL_DICT.values())

for keys in FULL_DICT:
    if FULL_DICT[keys]==MAX:
        print(keys, FULL_DICT[keys])

L=0
Students=[]
with open('C:/Users/SH/Downloads/dataset_3363_4.txt') as Words:
    for line in Words:
        Students.append(line.strip().split(';'))
        L+=1
print(L)

for i in range(L):
    Middle = (float(Students[i][1]) + float(Students[i][2]) + float(Students[i][3])) / 3
    print(Middle)
Middle_1=0
Middle_2=0
Middle_3=0
for i in range(L):
    Middle_1 = Middle_1+ float(Students[i][1])
    Middle_2 = Middle_2+ float(Students[i][2])
    Middle_3=  Middle_3+ float(Students[i][3])
print(f'{Middle_1/L} {Middle_2/L} {Middle_3/L}')

