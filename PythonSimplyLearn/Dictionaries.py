'''keys:value
unordered groups
mutable- can be changed
like associative arrays'''
gradeDict={'kelly':89,'David':65,'Jackk':95,"sam":78}
print(gradeDict)
print(gradeDict['David'])
gradeDict['David']=56
print(gradeDict)
gradeDict['jess']=92
print(gradeDict)
gradeDict['cat']=77
print(gradeDict)
del gradeDict['David']
print(gradeDict)

gradeDict={'kelly':[89,88],'Jackk':[95,23],"sam":[78,77],"jessy":[22,33]}
print(gradeDict)
print(gradeDict['jessy'])
print(gradeDict['Jackk'][0])
del gradeDict['Jackk'][1]
print(gradeDict)
del gradeDict['jessy']
gradeDict['kelly'][0]=(88)
print(gradeDict)
gradeDict['kelly'][0]=[21]
print(gradeDict)
gradeDict['kelly']=[21,334]
print(gradeDict)
gradeDict['kelly'][0]='jelly'
print(gradeDict)