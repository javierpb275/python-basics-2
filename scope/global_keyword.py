# Scope - what variables do I have access to?

total = 0


def count():
    global total
    total += 1
    return total


count()
print(count())  # 2

# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - built in python functions
