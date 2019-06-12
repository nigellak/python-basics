#prime numbers between 10 and 50

from math import *

#
# for num in range(10, 50):
#     if num % num == 1:
#         print(num)

# n= input("first number")


# if( n is > 1) :
# if n % 2, 3, ..., n - 1 == 0:
#         print(not_prime)

# i = 2
# if n % i == 0:
#     print('not prime')

for num in range(1,50):
    # print(num)
    if num == 2 or num == 3 or num == 5 or num == 7 :
        print(num)
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        print(num)