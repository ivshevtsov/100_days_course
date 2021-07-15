import random

#41
print('#Video 41#')
str_names = 'Angela, Ben, Jenny, Michael, Chloe'
names = str_names.split(', ')
number_names = len(names)
number = random.randint(0, number_names)
print(f'{names[number-1]} is going to win today!')

#44
print('#Video 44#')

map = ['⬜', '⬜', '⬜']
map_1=['⬜', '⬜', '⬜']
A=22
string = int(A/10)
column = int(A%10)

print('First method')
for i in range(len(map)):
    if i==string-1:
        map_1[column-1]= 'O'
        print(map_1)
    else:
        print(map)
print('Second method')
row_1 = ['⬜', '⬜', '⬜']
row_2 = ['⬜', '⬜', '⬜']
row_3 = ['⬜', '⬜', '⬜']
massive = [row_1, row_2, row_3]
mas_string = massive[string-1]
mas_string[column-1]='X'
print(f'{row_1}\n{row_2}\n{row_3}')


#45
print('#Video 45#')

Rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

Paper = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

Values=[Rock, Scissors, Paper]

Your_chiose = int(input('Input your choise Rock(0)/scissors(1)/paper(2):'))
Comp_choise = random.randint(0, len(Values)-1)


if Your_chiose<Comp_choise and abs(Your_chiose-Comp_choise)==1:
    print('You win')
    print('Your choose')
    print(Values[Your_chiose])
    print('Computer choose')
    print(Values[Comp_choise])

elif Your_chiose>Comp_choise and abs(Your_chiose-Comp_choise)==2:
    print('You win')
    print('You choose')
    print(Values[Your_chiose])
    print('Computer choose')
    print(Values[Comp_choise])

elif Your_chiose==Comp_choise:
    print('Repeat')
    print('You choose')
    print(Values[Your_chiose])
    print('Computer choose')
    print(Values[Comp_choise])

else:
    print('You lose')
    print('You choose')
    print(Values[Your_chiose])
    print('Computer choose')
    print(Values[Comp_choise])






