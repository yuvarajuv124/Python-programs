def add(a,b):
    print('Sum is:',a+b)
def subtraction(a,b):
    print('Difference is:',a-b)
def multiplacation(a,b):
    print('Product is:',a*b)
def division(a,b):
    print('Division is:',a/b)
num1= int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
value = int(input('Enter the number for your operation: '))
if value==1:
    add(num1,num2)
elif value==2:
    subtraction(num1,num2)
elif value==3:
    multiplacation(num1,num2)
elif value==4:
    division(num1,num2)
else:
    print('Enter valid number.')

