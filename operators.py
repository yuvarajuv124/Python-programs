'''
a = input("Enter your name : ")
b = input("Enter your age : ")
print(a,b,type(a),type(b))
'''
x = 10
y = 2
print('==> Arithmetic Operators:')
print("sum =",x+y)
print("subtraction =",x-y)
print("Multiplication =",x * y)
print("Division =",x/y)
print("Floor division =",x//y)
print('Power =',x**y)

print('==>Comparision Operators')
print("x>y :",x>y)
print('x<y :',x<y)
print('x==y :',x==y)
print('x!=y :',x!=y)

print('==> Logical Operators')
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

''' x= 10 -> 1010
    y = 2 -> 0010
       x&y = 0010
       x|y = 1010
       ~x =  '''
print('==> Bit wise Operators')
print(x & y)
print(x | y)
print(~x)
print(x ^ y)
print(x>>2)
print(x<<2)

print('==> Assignment operators')
c = 25
c += 2
print(c)
c = 25
c -= 5
print(c)

