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
"""
print(not(True))  # False
