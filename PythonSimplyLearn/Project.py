import statistics

admins = {'Python':'Pass123','user2':'pass2'}
studentDict={'Jeff':[78,88,93],
             'Alex':[92,76,88],
             'Sam':[89,92,93]}
def enterGrades():
    nameToEnter=input('Student Name: ')
    gradeToEnter=input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist')    
    print(studentDict) 

def removeStudent():
    nameToRemove = input('What student to remove?: ')
    if nameToRemove in studentDict:
        print('removing student...')
        del studentDict[nameToRemove]
    print(studentDict)  

def studentAvgs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade =statistics.mean(gradeList)
        print(eachStudent,'has an average grade of : ',avgGrade)
    print(studentDict)    

def main():
    print("""
    Welcome to grade central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)
    action = input("What would you like to do today? (Enter a number) ")

    if action=="1":
        enterGrades()
    elif action=="2":
        removeStudent()
    elif action=="3":
        studentAvgs()   
    elif action=="4":
        exit()
    else:
        print("no valid choice")  

login = input('username: ')    
passw = input('password: ')        

if login in admins:
    if admins[login]==passw:
        print('Welcom',login)
        while True:          
            main()
    else: 
        print('Invalid password, will detonate in 5 seconds!')    
else:
    print('Invalid username, calling the FBI to report this ')        
