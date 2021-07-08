
#27
print('#Video 27#')
#conditional statements
'''
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm?'))
if height>=120:
    print('Pass')
else:
    print('No Pass!')
'''

#28
print('#Video 28#')
'''
Number = int(input('Enter number: '))
if Number%2 == 0:
    print('This is a even number')
else:
    print('This is an odd number')
'''

#29
print('#Video 29#')
#calculate ticket price
'''
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm?'))
if height>=120:
    age = int(input('How old are you?'))
    if age<12:
        print('Pass. Pay 5$')
    elif age<=18:
        print('Pass. Pay 7$')
    else:
        print('Pass. Pay 12$')
else:
    print('No Pass!')
'''

#30
print('#Video 30#')
#interpretate body mass index(BMI)
'''
weight = int(input('Input your weight, kg:'))
height = int(input('Input your height, cm:'))/100
BMI = round(weight/(height**2), 2)
print(f'Your BMI: {BMI}')
if BMI <= 18.5:
    print('Underweight')
elif BMI <= 25:
    print('Normal weight')
elif BMI <= 30:
    print('Slightly overweight')
elif BMI <= 35:
    print('Obese')
else:
    print('Clinical obese')
'''

#31
print('#Video 31#')
'''
Year = int(input('Year: '))
if Year%4 ==0:
    if Year%100 == 0:
        if Year%400==0:
            print('Leap year')
        else:
            print('No Leap Year')
    else:
        print('Leap year')
else:
    print('No Leap Year')
'''

#32
print('#Video 32#')
'''
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm?'))
bill=0
if height>=120:
    age = int(input('How old are you?'))
    if age<12:
        print('Child tickets is 5$')
        bill = 5
    elif age<=18:
        print('Yoth tickets is 7$')
        bill = 7
    else:
        print('Adult tickets is 12$')
        bill = 12

    wants_photo = input('Do you want a photo taken? Y/N.')

    if wants_photo.lower() =="y" or wants_photo.lower() =="yes" :
        bill+=3
        print(f'Pass. Pay {bill}$')
    else:
        print(f'Pass. Pay {bill}$')
else:
    print('No Pass!')
'''

#33
print('#Video 33#')
#buy pizza
'''
size = input('Input size pizza. Small/Medium/Large:')
Bill=0
if size.lower()=='small':
    Price = 15
    Bill=Bill+Price
    print(f'{size} Pizza is ${Price}')
elif size.lower()=='medium':
    Price = 20
    Bill = Bill + Price
    print(f'{size} Pizza is ${Price}')
elif size.lower()=='large':
    Price = 25
    Bill = Bill + Price
    print(f'{size} Pizza is ${Price}')
else:
    print('Incorrect size')

pepperoni = input('Do you want a pepperoni.(Y/N).')
if pepperoni.lower() == 'y':
    if size.lower()=='small':
        Bill += 2
        print('Add peperoni +$2')
    else:
        Bill += 3
        print('Add peperoni +$3')
else:
    print('Pepperoni +$0')

cheese = input('Do you want extra cheese? (Y/N)')
if cheese.lower() == 'y':
    Bill += 1
    print('Add cheese +$1')
else:
    print('Pepperoni +$0')

print(f'Total bill:${Bill}')
'''

#34
print('#Video 34#')

#35
print('#Video 35#')
#love calculator
'''
Word_1 = 'true'
Word_2 = 'love'
name_1 = input('Input first name:')
name_2 = input('Input second name:')
total_name = (name_1+name_2).lower()

sum_1=0
sum_2=0
for i in range(len(Word_1)):
    for k in range(len(total_name)):
        if total_name[k].isalpha()==True and total_name[k]==Word_1[i]:
            sum_1+=1

for i in range(len(Word_2)):
    for k in range(len(total_name)):
        if total_name[k].isalpha()==True and total_name[k]==Word_2[i]:
            sum_2+=1

Score = int(str(sum_1)+str(sum_2))

if Score<10 or Score>90:
    print(f'Your score is {Score}, you go together like coke and mentos.')
elif Score>=40 and Score<=50:
    print(f'Your score is {Score}, you are alright together.')
else:
    print(f'Your score is {Score}')
'''

#36
print('#Video 36#')
#Final project
Text_question_1 = "You're at a cross road. Where do you want to go? Type 'left of 'right'\n"
Text_question_2 = "You come to a lake. There is an island in the middle of the lake\n" \
                  "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
Text_question_3 = "You are arrived at the island unharmed. There is a house with 3 doors.\n" \
                  "One red, one yellow and one blue. Which colour do you choose?\n"
#Win pictire
WIN = r'''
 _    _ _____ _   _ 
| |  | |_   _| \ | |
| |  | | | | |  \| |
| |/\| | | | | . ` |
\  /\  /_| |_| |\  |
 \/  \/ \___/\_| \_/
'''
#Game over picture
Over = r'''
   _____                                          
  / ____|                                           
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
'''
#Start picture
Start = r'''
                              _.-.
                             /  99\
                            (      `\
                            |\\ ,  ,|
                    __      | \\____/
              ,.--"`-.".   /   `---'
          _.-'          '-/      |
      _.-"   |   '-.             |_/_
,__.-'  _,.--\      \      ((    /-\
',_..--'      `\     \      \\_ /
                `-,   )      |\' 
                  |   |-.,,-" (  
                  |   |   `\   `',_
                  )    \    \,(\(\-'
                  \     `-,_
                   \_(\-(\`-`
                      "  "
'''

print(Start)
print('Welcome to Tresure Island')
print('Your mission to find treasure')
if input(Text_question_1).lower() == 'left':
    if input(Text_question_2).lower() == 'wait':
        if input(Text_question_3).lower() == 'yellow':
            print(WIN)
        else:
            print(Over)
    else:
        print(Over)
else:
    print(Over)














