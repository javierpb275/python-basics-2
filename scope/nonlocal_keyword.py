# Scope - what variables do I have access to?
def outer():
    x = "local"
    def inner():
        nonlocal x #grab variable x from my parent's scope
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)


outer()

#result:
#inner: nonlocal
#outer: nonlocal

# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - built in python functions
