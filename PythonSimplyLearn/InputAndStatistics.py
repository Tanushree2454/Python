#input from user
# name = input('What is your name?')
# print('my name',name)

import statistics

exList=[2,5,3,2,9,5,2,4,2,1]

x=statistics.mean(exList)
print(x)
x=statistics.median(exList)
print(x)
x=statistics.mode(exList)
print(x)
x=statistics.stdev(exList)
print(x)
x=statistics.variance(exList)
print(x)

#import syntax

import statistics

exList=[2,5,3,2,9,5,2,4,2,1]
print(statistics.mean(exList))

#or

import statistics as s 

print(s.mean(exList))

#or

from statistics import mean

print(mean(exList))

#or

from statistics import mean as m

print(m(exList))

#or

from statistics import mean,stdev

print(mean(exList))
print(stdev(exList))

#or

from statistics import mean as m ,stdev as s

print(m(exList))
print(s(exList))

#or

from statistics import *

print(mean(exList))
print(stdev(exList))
print(median(exList))
print(mode(exList))
print(variance(exList))

