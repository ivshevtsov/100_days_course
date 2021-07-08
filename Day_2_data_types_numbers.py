#17
print('#Video 17#')
#Data types
#string
print('Hello'[-1])
print(type('Hello'))
print('123' + '345')

#integer
print(123 + 345)
print(type(123))

#float
print(3.14159)
print(type(3.14159))

#Boolean
print(True)
print(type(True))

#18
print('#Video 18#')
#num_char = len(input('What is your name?'))
#print('Your name has ' + str(num_char) + ' characters.')

#19
print('#Video 19#')
'''
Number = input('Two digit number:')
Sum=0
for i in range(len(str(Number))):
    Sum = int(str(Number[i]))+Sum
print(f'Result:{Sum}')
'''

#20
print('#Video 20#')
#mathematical operations
#+ - / * **
print(type(3/2))
print(2**4)

#21
print('#Video 21#')
#Body mass index (BMI)
#BMI = weight/heigth^2
'''
weigth = float(input('Input your weight, kg:'))
height = float(input('Input your height, cm:'))/100
BMI = round(weigth/(height**2), 2)
print(f'Your BMI is: {BMI}')
if BMI<18.5:
    print('You have low weigth')
elif BMI>=18.5 and BMI<=24.9:
    print('You have normal weigth')
elif BMI>=25 and BMI<=29.9:
    print('You have high weigth')
else:
    print('You are fat')

'''

#22
print('#Video 22#')
print(round(2.6666, 2))
print(8//3)
print(type(8//3))
k=1
k+=1
print(k)

#23
print('#Video 23#')
#how many years you will live
'''
age = int(input('What is your current age?:'))
end_age = 90
end = end_age-age
print(f'You have a:\n {end} years or\n {end*12} month '
      f'or\n {end*12*30} days or\n {end*12*30*24} hours')
'''

#24
print('#Video 24#')
'''
#calculate tips
print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill?'))
percent_bill = int(input('What percentage tip would you like give? 10, 12 or 15?'))
n_people = int(input('How many people to split the bill?'))
result = total_bill*(1+percent_bill/100)/n_people
print(f'Each person should pay: ${round(result,2)}')
'''































