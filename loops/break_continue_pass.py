my_list = [1, 2, 3]
for item in my_list:
    print(item)  # 1
    break

i = 0
while i < len(my_list):
    print(my_list[i])  # 1
    i += 1
    break

for item in my_list:
    continue  # it goes back to the beginning of the loop
    print(item)  # so this never gets executed

j = 0
while j < len(my_list):
    j += 1
    continue  # it goes back to the beginning of the loop
    print(my_list[j])  # so this never gets executed

#pass does absolutely nothing. you can use it for example as a placeholder (like a comment):
for item in my_list:
    pass
    print(item)  # 1, 2, 3

k = 0
while k < len(my_list):
    print(my_list[k])  # 1, 2, 3
    k += 1
    pass
