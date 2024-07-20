#tuple-immutable- cannot be changed - used for sequence unpacking, (takes up less space, u can iterate through the items of a tuple faster than a list) 

def example():
     return 15,19
    #or   return (15,19)

a,b=example()
print(a)
print(b)

#list-mutable- can be changed

x=[6,2,3,6,8,9,4,3]
print(x)
print(x[5])
x.append(12)#add
print(x)
x.insert(5,7)
print(x)
x.remove(6)#if you have multiple 6's it won't remove all of the 6's it will only remove the first 6 that appears in the list
print(x)
print(x.index(12))
print(x.count(3))
x.sort()
print(x)
x.reverse()
print(x)

x=['sport','cam','jan','dive','zack']
print(x)
x.reverse()
print(x)
x.sort()
print(x)
x.reverse()
print(x)
