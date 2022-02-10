# -*- coding: utf-8 -*-
"""
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

k = 2
power = 1000
number = k**power

number=str(number)
final_result = 0


for n in number:
    final_result += int(n) 

print(final_result)       
        
#%%
"""
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""
numbers = {'1': 'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':
           'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':
               'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen',
               '19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty','60':
                   'sixty','70':'seventy','80':'eighty','90':'ninety','100':'hundred',
                   '1000':'thousand'}
result = 0

for i in range (1, 1001):
    if i < 20:
        result += len(numbers[str(i)])
        
        
    elif i < 100:
        if i % 10 == 0:
            result += len(numbers[str(i)])
            
        else:
            num1 = numbers[str(i%10)]
            num2 = numbers[str((i//10)*10)]
            num_str = num2+num1
            print(num_str)
            result += len(num_str)
            
    elif i <= 999:
        if i % 100 == 0:
            result += len(numbers[str(int(i/100))])+len(numbers[str(int(i/(i/100)))])
            
        else:
            nlist = list(str(i))
            print(numbers[nlist[0]])
            print(numbers['100'])
            result += len(numbers[nlist[0]])
            result += len(numbers['100'])
            result += 3
            last_two = nlist[1:3]
            if last_two[0] == '0':
                last_two.pop(0)
            last_two = ''.join(last_two)
            if int(last_two) < 20:
                result += len(numbers[last_two])
                
            elif int(last_two) < 100:
                if int(last_two) % 10 == 0:
                    result += len(numbers[last_two])
                    
                else:
                    num1 = numbers[str(int(last_two)%10)]
                    num2 = numbers[str((int(last_two)//10)*10)]
                    num_str = num2+num1
                    print(num_str)
                    result += len(num_str)
                    
    elif i == 1000:
        result += len(numbers['1'])
        result += len(numbers['1000'])
                    




#%%
"""
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

               75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by 
trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
"""

triangle = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

triangle.reverse()

for i in range(0, len(triangle)-1):
    
    index = 0
    while index < len(triangle[i])-1:    
        
        if triangle[i][index] > triangle[i][index+1]:
            triangle[i+1][index] = triangle[i][index] + triangle[i+1][index]
            
        else:
            triangle[i+1][index] = triangle[i][index+1] + triangle[i+1][index]
            
        index += 1


print("The result is", triangle[14][0])
    

#%%
"""
Problem 19
You are given the following information, but you may prefer to do some research 
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?  
"""
weekdays = ['monday','tuesday','wedensday','thursday', 'friday','saturday','sunday']

sundays_on_the_first = 0


month = 1
year = 1900

while year != 2001:
    counter = 0
    while month <= 12 and year != 2001:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
            for day in range(1,32):
                if counter == 7:
                    counter = 0
                weekday = weekdays[counter]
                counter += 1
                if year > 1900:
                    if day == 1 and weekday == 'sunday':
                        sundays_on_the_first += 1
            month += 1
    
                
        if month == 2:
            if year%4 == 0:
                if year%100 != 0 or year%400 == 0:
                    for day in range(1, 30):
                        if counter == 7:
                            counter = 0
                        weekday = weekdays[counter]
                        counter += 1
                        if year > 1900:
                            if day == 1 and weekday == 'sunday':
                                sundays_on_the_first += 1
                    month += 1   
                else:
                    for day in range(1,29):
                        if counter == 7:
                            counter = 0
                        weekday = weekdays[counter]
                        counter += 1
                        if year > 1900:
                            if day == 1 and weekday == 'sunday':
                                sundays_on_the_first += 1
                    month += 1
                    
            else:
                for day in range(1,29):
                    if counter == 7:
                        counter = 0
                    weekday = weekdays[counter]
                    counter += 1
                    if year > 1900:
                        if day == 1 and weekday == 'sunday':
                            sundays_on_the_first += 1
                month += 1
                
        if month == 9 or month == 4 or month == 6 or month == 11:
            for day in range(1,31):
                if counter == 7:
                    counter = 0
                weekday = weekdays[counter]
                counter += 1
                if year > 1900:
                    if day == 1 and weekday == 'sunday':
                        sundays_on_the_first += 1
            month += 1
         
        if month == 12:    
            for day in range(1,32):
                if counter == 7:
                    counter = 0
                weekday = weekdays[counter]
                counter += 1
                if year > 1900:
                    if day == 1 and weekday == 'sunday':
                        sundays_on_the_first += 1
            month = 1
            year += 1        
print(sundays_on_the_first)
        
 #%%
"""
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!        
"""

n = 100
product = 1
result = 0
for i in range(n, 0, -1):
    product *= i
    
for number in str(product):
    result += int(number)

print(result)       