print("hello world!")
print("hello world!")
print("2nd commit for before working")

ex_8 = "orange"
print(ex_8[2])
print("apple"[4])

ex_10 = "apricots"
## string slicing
print(ex_10[:3])
print(ex_10[2:5])
print(ex_10[4:])
r2d2 = "R2" + "-" + "D2"
print(r2d2)

##type()
ex_6 = 3.21 
print(type(ex_6))
new_ex_6 = str(ex_6)
print(type(new_ex_6))

##escape sequences
## \t tab -> sen c bilen adamsin bunu mu bilmeyeceksin

#'input
name = input("enter name\n")
print(" your name " + name + ".")
print("fav number") #trying with c style
number = input()
print("fav => "+ number)

# int() and fload() basic converting
# satir 20'deki gibi.. int ve floati da biliyorsun
use_int = int(input("Please enter an integer."))
print(use_int + 10)
print(int(use_int) + 10)

## FUNCTION 
# def func name(var):
# 4 spaces inside
# 
#  2 blank lines to end the function

##
# 
# auto comment, start with double #
# 
##

def function_try(input_var):
    print("input var with function = ")
    print(input_var+2)


function_try(8)

# my addition for function test
test_a = "SR-71"

def function_try_2(input_var, input_str):
    print("input str" + str(input_str) +" and var with function = "+ str(input_var + 2))


function_try_2(8,test_a)

## defaultparameters
# exampli gratia 2 parameeters were defined and we can pass up to 2 paraeters
# if we pass 0 parameter defaults work
# if we pass 1 parameter 1st parameter replaces with inpu and 2nd will be default one
# if we pass 2 parameter inputs work, defaults wouldnt be needed
# if we pass more than defined parameters complie ERROR
# 
# 
# ## 
# 
# continue 

print("c")
