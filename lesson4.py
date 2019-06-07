x= input("first number")
y= input("second number")

print(type(y))

if x.isnumeric() and y.isnumeric():
    x_num = float(x)
    y_num = float(y)
    print(x_num +y_num)

else:
    print('invalid values')