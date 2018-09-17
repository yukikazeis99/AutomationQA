# -*- encoding=utf8 -*-
__author__ = "VAGRANT"

from airtest.core.api import *

auto_setup(__file__)

# create Loop command scripts tutorial on python by VAGRANT
print('==========================================================================')
print('''___ ___  ____  _____      __     ___    ____ ____      _    _   _ _____ 
  / ___/ _ \|  _ \| ____|  _  \ \   / / \  / ___|  _ \    / \  | \ | |_   _|
 | |  | | | | | | |  _|   (_)  \ \ / / _ \| |  _| |_) |  / _ \ |  \| | | |  
 | |__| |_| | |_| | |___   _    \ V / ___ \ |_| |  _ <  / ___ \| |\  | | |  
  \____\___/|____/|_____| (_)    \_/_/   \_\____|_| \_\/_/   \_\_| \_| |_|''')
print('==========================================================================')

def function1():
    test = ['banana','apple','microsoft']
    test2 = [20,10,5]
    #for string
    for element in test:
        print(element)
    #for number
    for element2 in test2:
        print(element2)


#function1()
#=====================================================
def function2():
    b = [20, 10, 5]
    total = 0
    for e in b:
        #print(e)
        total = total + e
    print(total)
function2()
#=====================================================
def function3():
    #1, 2, 3, 4
    c = list(range(1, 5)) #not including 5
    print(c)
    
    
#function3()    
#=====================================================
def function4():
    num2 = 0
    for i in range(1, 5):
        #print(i)
        total2 += i
    print(num2)

#function4()
#=====================================================
def function5():
    print(list(range(1, 8)))
    
    #what if the % ?????
    #print(4 % 3)
    #the result is 1
    #print(5 % 3)
    #the result is 2
    #print(1 % 3)
    #the result is 1
    #print(6 % 3)
    #the result is 0

#function5()
#=====================================================
def function6():
    total3 = 0
    for i in range(1, 8):
        if i % 3 == 0:
            total3 += i
    print(total3)
#function6()
#=====================================================
print('Python Code stopped, Vagrant code was here!!')