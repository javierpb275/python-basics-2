def print_sth(sth):
    '''
    Info: this function prints the argument that we pass
    '''
    print(sth)


help(print_sth)

'''
Help on function print_sth in module __main__:

print_sth(sth)
    Info: this function prints the argument that we pass

'''

print(print_sth.__doc__)  # Info: this function prints the argument that we pass


# clean code:

def is_even(num):
    return num % 2 == 0


print(is_even(50))  # True
