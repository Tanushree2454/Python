

def example():
    x=1
    y=3
    print(x+y)

    if x<y:
        print(x,'is less than',y)

def main():
    example()

def addition(num1,num2,num3,num4):
    answer =num1+num2+num3+num4
    return answer

def website(font,background_color,font_size,font_color):
    print('font:',font)
    print('bg:',background_color)
    print('Font size',font_size)
    print('Font color',font_color)

def websites(font_color='black',
        font='TNR',
        background_color='yellow',
        font_size='11'):
    print('font:',font)
    print('bg:',background_color)
    print('Font size',font_size)
    print('Font color',font_color)

# websites()  
# websites(background_color='grey')     
# website('TNR','white','11','black')
# website(font_color='black',
#         font='TNR',
#         background_color='white',
#         font_size='11')    


# main()    
# x= addition(2,3,4,5)
# print(x)

# global and local variables
x=6
def example3():
    global x
    x+=1
    print(x)
print("after example 3")    
example3()    
print("hellow")
def example():
    z=5
    print("z",z)

# example()
# print(z), local variable
# print("x",x)
def example2():
    z=7
    print("z",z)
    print("x",x)
    # x+=1//not possible
    # print(x)
    y=x+1
    print("y",y)
    return y
# print("x",x)
x=example2()
# print("x",x)
example2()    
print(x)


# Errors -:
# '''exception error-- is gonna let the code run up untill the exception
print('string here')
#NameError
'''
variable =55
print(variabel)
'''

#    syntax error-- wont allow the code to run at all'''

#expected an indent
'''
def func1():
def func2():
    print(2)
    '''
# parent function child function this code will run without an error
def func1():
    def func2():
        print(2)

#unexpected Indent
'''
def task():
    print('1')
print('2')    
    print('3')
    '''
# typos (example-missing clossing brackets)
# print('hey im tanushree'
# x = [1,2,34,44 




appendMe ='even some more text'
saveFile = open('exampleFile.txt','a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()



