
# range(stop) -> range object range(start, stop[, step]) -> range object
print(range(100))  # range(0, 100)
print(range(0, 100))  # range(0, 100)

# you can iterate over a range() object:
for number in range(0, 10):
    print(number)  # 0, 1, 2... 9

for _ in range(0, 10, 2):
    print(_)  # 0, 2, 4, 6, 8

for _ in range(10, 0, -1):
    print(_)  # 10, 9, 8... 1

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
