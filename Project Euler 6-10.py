# -*- coding: utf-8 -*-
"""
Problem 6

Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum
"""
lst1 = []
lst2 = []
n = 100
for i in range (1, n+1):
    lst1.append(i)
    lst2.append(i**2)
a = sum(lst1)**2
b = sum(lst2)

print("The difference of the square of the sum and the sum of the square of the numbers from 1 to: ", n, "is: ", a - b)

#%%
"""
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
import time

def nth_prime(n):
    start = time.time()
    primelist = [2]
    next_num = 3
    while len(primelist) < n:
        for p in primelist:
            if next_num%p == 0:
                break
        else:
            primelist.append(next_num)
        next_num += 2
    end = time.time()
    print("took: ", end-start, " seconds")
    return primelist[-1]

print(nth_prime(10001))




#%%

""" 
Problem 8

The four adjacent digits in the 1000-digit number that have the greatest 
product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number
that have the greatest product. What is the value of this product?
"""

p = [7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450]
plist = list(str(p)) #(splitter listen)
flatlist = []
for i in plist:
    if i != '[' and i != ']':
        flatlist.append(int(i))    


resultlist = []
n = len(flatlist) # Definerer længden på listen
connum = 13 # antallet af på hinanden følgende tal, som skal udregnes
connum1 = connum-1

result = 0 # resultatet af produktet
prod = 1

for i in range(0, n-connum1):
    for k in range(0, connum):
        resultlist.append(flatlist[k+i])
    if len(resultlist) == connum:
        for j in resultlist:
            prod = prod*j
        if prod > result:
            result = prod
        prod = 1
    resultlist.clear()

print(result)

#%%
""" 
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which, a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""



result = 0
result = 0
for a in range(1, 500):
    print(a)
    for b in range(1, 500):
        c2 = a**2 + b**2
        c = c2**0.5
        result = a+b+c
        if result == 1000:
            break
    if result == 1000:
        break
print(a, b, c)
print(a*b*c)


#%%
"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def sum_of_primes_below(n):
    start = time.time()
    prime_list = list(range(2, n+1))
    
    for i in range(2,int(n**0.5+1)):
        for number in prime_list:
            if number != 0:
                if number%i == 0 and number != i:
                    prime_list[number-2] = 0
    end = time.time()
    
    print(sum(prime_list))
    #print(list(filter(lambda a: a != 0, prime_list)))
    
    print("time used: ", end-start, " seconds")



sum_of_primes_below(2000000)


