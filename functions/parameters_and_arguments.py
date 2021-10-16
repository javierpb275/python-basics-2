# default parameters
def say_sth(sth="hello", name="pepe"):
    print(f'{sth} {name}')

say_sth()  # hello pepe

# positional arguments (because the position matters)
say_sth("hello", "pepe")

# keyword arguments
say_sth(name="paco", sth="hello")
