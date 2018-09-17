# -*- encoding=utf8 -*-
__author__ = "VAGRANT"

from airtest.core.api import *

auto_setup(__file__)

# Conditional command scripts tutorial on python by VAGRANT
print('==========================================================================')
print('''___ ___  ____  _____      __     ___    ____ ____      _    _   _ _____ 
  / ___/ _ \|  _ \| ____|  _  \ \   / / \  / ___|  _ \    / \  | \ | |_   _|
 | |  | | | | | | |  _|   (_)  \ \ / / _ \| |  _| |_) |  / _ \ |  \| | | |  
 | |__| |_| | |_| | |___   _    \ V / ___ \ |_| |  _ <  / ___ \| |\  | | |  
  \____\___/|____/|_____| (_)    \_/_/   \_\____|_| \_\/_/   \_\_| \_| |_|''')
print('==========================================================================')

def testCase1():
    a = 1
    b = 2
    if a < b:
        print ("a kurang dari b")
        print ('NOT SURE IF A LESS THAN b');
    print('belum pasti jika a kurang dari b');
    return;

#testCase1()

#=====================================================

def testCase2():
    c = 1
    d = 4
    if c < d:
        print('c kurang dari d')
    else:
        print('C IS NOT LESS THAN D')
        print('I dont think c is less than d');
    print('outside the if block')
    return;

#testCase2()

#=====================================================

def testCase3():
    e = 10
    f = 8
    if e < f:
        print('e kurang dari f')
    elif e == f:
        print('e sama dengan f');
    elif e > f + 10:
        print('e is greather than f by more than 10');
    else:
        print('e lebih besar dari f')
    return;

#testCase3()
#=====================================================

def testCase4():
    g = 7
    h = 6
    if g < h:
        print('g is less than h')
    else:
        if g == h:
            print('g sama dengan h')
        else:
            print('g is greater than h')
    return;

#testCase4()
#=====================================================    

def testCase5():
    name = "DK"
    height_m = 2
    weight_kg = 90
    
    bmi = weight_kg / (height_m * height_m)
    #bmi = weight_kg / (height_m ** 2)
    print('bmi: ')
    print(bmi)
    if bmi < 25:
        print(name)
        print('is not overweight')
    else:
        print(name)
        print('is overweight')
    return;
testCase5()
#=====================================================   

print('Python Code stopped, Vagrant code was here!!')

