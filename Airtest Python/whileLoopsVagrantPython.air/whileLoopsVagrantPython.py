# -*- encoding=utf8 -*-
__author__ = "VAGRANT"

from airtest.core.api import *

auto_setup(__file__)

# create while loop command scripts tutorial on python by VAGRANT
print('==========================================================================')
print('''___ ___  ____  _____      __     ___    ____ ____      _    _   _ _____ 
  / ___/ _ \|  _ \| ____|  _  \ \   / / \  / ___|  _ \    / \  | \ | |_   _|
 | |  | | | | | | |  _|   (_)  \ \ / / _ \| |  _| |_) |  / _ \ |  \| | | |  
 | |__| |_| | |_| | |___   _    \ V / ___ \ |_| |  _ <  / ___ \| |\  | | |  
  \____\___/|____/|_____| (_)    \_/_/   \_\____|_| \_\/_/   \_\_| \_| |_|''')
print('==========================================================================')

#Using Loop
def usingLoop():
    total = 0
    for i in range(1, 5):
        total += i
    print('total value is: ')
    print(total)

#usingLoop()
#=====================================================
#Using While
def usingWhile():
    total2 = 0
    j = 1
    while j < 5:
        total2 +=j
        j += 1
    print('total value is: ')    
    print(total2)

#usingWhile()
#=====================================================
def usingWhile2():
    #given_list = [5, 4, 4, 3, 1, -2, -3, -5]
    given_list = [5, 4, 4, 3, 1]
    total3 = 0
    i = 0
    #while given_list[i] > 0:
    #while i < 5 and given_list[i] > 0:
    while i < len(given_list) and given_list[i] > 0:
        total3 += given_list[i]
        i += 1
    print(total3)
    
#usingWhile2()
#=====================================================
def usingWhile3():
    given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
    total4 = 0
    for elemental in given_list2:
        if elemental <= 0:
            break
        total4 += elemental
    print(elemental)
    print(total4)
    
    
#usingWhile3()
#=====================================================
def usingWhile4():
    given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
    total5 = 0
    i = 0
    while True:
        total5 += given_list2[i]
        i += 1
        if given_list2[i] <= 0:
            break
    print(total5)       
usingWhile4()
#=====================================================
print('Python Code stopped, Vagrant code was here!!')