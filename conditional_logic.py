is_old = True
is_licenced = False

if is_old and is_licenced:
    print('you can drive now')
elif is_old:
    print('you are old enough to drive but you do not have a licence!')
else:
    print('you are not of age!')

print('okok')

#Truthy and Falsey

filled_string = "hello"  # True
bigger_than_0 = 5  # True

empty_string = ""  # False
cero = 0  # False
null = None  # False


# ternary operator

#condition_if_true if condition else condition_if_false
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)  # message allowed

# short circuiting (or)
is_Friend = False
is_User = True

if is_Friend or is_User:
    print("Welcome")

""" 
LOGICAL OPERATORS
  >          >=
  <          <=
  ==         !=
  and        or
  not 

print(not(True))  # False
print(not False)  # True
"""

""" 
# is vs ==

# == checks for equality of value
print(True == 1)  # True
print('' == 1)  # False
print('1' == 1)  # False
print(bool([]))# [] is false
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True
print([1,2,3] == [1,2,3])  # True

# is checks if the location in memory is the same
print(True is 1)  # False
print('' is 1)  # False
print('1' is 1)  # False
print(bool([]))# False
print([] is 1)  # False
print(10 is 10.0)  # False
print([] is [])  # False
print([1,2,3] is [1,2,3])  # False
#everytime we create a [], it is created in a new location in memory
 """