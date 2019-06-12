from math import  sqrt
# functions
def add(x, y):
    print(x + y)

add(4,5)
add(6,88)

def sayHi():
    print("Hey")

sayHi()
sayHi()

def area(b):
    x=(sqrt(3)/4)*b**2
    # print(x)
    return x

z=area(10)
print(z, 'is my area')

def volume(r, h, PI=3.14):
    v = PI*r**2*h
    return v

print(volume(7,7))
print(volume(7,7, 3.142))

def sum(x, y):
    total = 0
    for num in range (x, y+1):
        # print(num)ranges dont add the last num
        total = total + num

    print(total)
sum(10, 47)


