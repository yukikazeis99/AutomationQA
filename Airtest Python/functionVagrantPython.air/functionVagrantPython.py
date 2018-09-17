# -*- encoding=utf8 -*-
__author__ = "VAGRANT"

from airtest.core.api import *

auto_setup(__file__)

# create function command scripts tutorial on python by VAGRANT
print('==========================================================================')
print('''___ ___  ____  _____      __     ___    ____ ____      _    _   _ _____ 
  / ___/ _ \|  _ \| ____|  _  \ \   / / \  / ___|  _ \    / \  | \ | |_   _|
 | |  | | | | | | |  _|   (_)  \ \ / / _ \| |  _| |_) |  / _ \ |  \| | | |  
 | |__| |_| | |_| | |___   _    \ V / ___ \ |_| |  _ <  / ___ \| |\  | | |  
  \____\___/|____/|_____| (_)    \_/_/   \_\____|_| \_\/_/   \_\_| \_| |_|''')
print('==========================================================================')

# a collection of instructions
# a collection of code

def function1():
    print('ahhhh')
    print('ahhhhh 2')
#print('this is OUTSIDE the function')

#function1()
#function1()
#=====================================================
# a mapping
# input or an argument
def function2Total():
    def function2(value):
        return 2*value

    a = function2(3)
# return value or output
    print('the value of a is :  ')
    print(a)

    b = function2(4)
    # return value or output
    print('the value of b is :  ')
    print(b)

    #d = function2() <--- ERROR due to need required positional argument: 'value'

#function2Total()
#===================================================== 
def function3Total():
    def function3(a, b):
        return a + b
# return value or output
    e = function3(1, 2)
    print('the value of e is :  ')
    print(e)

#function3Total()
#===================================================== 
def function4Total():
    def function4(a):
        print(a)
        print('still in this function')
        return 3*a

    f = function4(4) #will be still in this function
    print(f) #generate return 3*a

#function4Total()
#=====================================================
def function5(some_argument):
    print(some_argument)
    print('weeeeeeee')
    
#function5(4)
#=====================================================
# BMI Calculator
def function6():
    #Local Variable start here
    name1= "DK"
    height_m1= 2
    weight_kg1= 90
    
    name2= "NAVI"
    height_m2= 1.8
    weight_kg2= 70
    
    name3= "EHOME"
    height_m3= 2.5
    weight_kg3= 160
    #Function related bmi_calculator here
    def bmi_calculator(name, height_m, weight_kg):
        bmi = weight_kg / (height_m ** 2)
        #bmi = weight_kg / (height_m *height_m)
        print('bmi: ')
        print(bmi)
        if bmi < 25:
            return name + " not overweight"
        else:
            return name + " is overweight"
    result1 = bmi_calculator(name1, height_m1, weight_kg1)
    result2 = bmi_calculator(name2, height_m2, weight_kg2)
    result3 = bmi_calculator(name3, height_m3, weight_kg3)
    print(result1) 
    print(result2)
    print(result3)
    
#function6()
#=====================================================

print('Python Code stopped, Vagrant code was here!!')


