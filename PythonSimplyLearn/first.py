
print("Hello World")
print('Single Quotes')
print("concatena"+"tion")
print("hello","there")
print("I am",5)
# print("I am"+5)
# print(5+"I am")
print('I\'m 5')
# print('I'm 5')
print("I\'m 5")
print('He said "hi"')
print(1+3)
print(1-3)
print(1*3)
print(1/3)
print(1.5/3.6)
print(4**2)

exVar='100'
print(exVar)
exVar=100
print(exVar)

opVar=exVar/5.3
print(opVar)
_100ma=5
print(_100ma)
#single line comment
'''multiple
lline 
comment
'''

condition=1
while condition<10:
    print(condition)
    condition+=1

exampleList = [1,6,7,3,6,9,0]
for x in exampleList:
    print(x)

for y in range(1,11):
        print(y)


x=2
y=7
z=10
if x>y:
    print(x,"is greater than",y)
if y>x:
     print(x,"is less than ",y)
if x==y:
    print(x,"is the same as ",y)
if x=='2':
    print(x,"is the same as ",y)
if x<=y:
    print(x,'is less than or equal to',y)    
if z>y>x:
    print(z,'is greater than',y,'which is greater than',x)    
    
if z>y>x<=z>y:
    print(z,'is greater than',y,'which is greater than',x)       

x=13
y=6
if x<y:
    print(x,'is less than',y)    
if x>y:
    print(x,'is greater than',y)    
else:
    print(x,'is not less than',y)    
x=3
y=7
z=10
if x>y or x<z:
    print(x,'is greater than',y)    
elif x<z and z<y:
    print(x,'is less than',z)    
elif y<z:
    print(y,'is less than',z)    
else:
    print('nothing was the case')    