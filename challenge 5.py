x = input("Enter a number")

num = int(x)
if num == 2 or num == 3 or num == 5 or num == 7:
    print('prime')
elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print('prime')
else:
    print("not prime")