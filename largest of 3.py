# Program to find largest of give 3 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if(num1>num2 and num1>num3):
    print('num1 is the greatest number')
elif(num2>num3):
    print('num2 is the greatest')
else:
    print('num3 is the greatest number')
   


largest = num1 if(num1>num2 and num1>num3) else(num2 if(num2>num3) else num3)


       
