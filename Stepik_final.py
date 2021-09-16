
'''
List_1 = list(input())
List_2 = list(input())

Coding = dict(zip(List_1,List_2))
Decoding = dict(zip(List_2,List_1))

List_coding = input()
List_decoding = input()

#coding
Word_1=''
for i in range(len(List_coding)):
    Word_1 = Word_1 + Coding[List_coding[i]]
#decoding
Word_2=''
for i in range(len(List_decoding)):
    Word_2 = Word_2 + Decoding[List_decoding[i]]

print(Word_1)
print(Word_2)

'''


Words = set()
Words_out = set()
STR = ''
STR_LIST=[]
d = int(input())
while d>0:
    Words.add(input().lower())
    d-=1
l = int(input())
while l>0:
    STR= STR + input().lower().strip() + ' '
    l-=1
STR_LIST= STR.split()

for i in STR_LIST:
    if i not in Words and i not in Words_out:
        print(i)
        Words_out.add(i)

