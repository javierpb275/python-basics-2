# while loops:

i = 0
while i < 10:
    print(i)  # 0, 1, 2... 9
    i += 1

j = 0
while j < 15:
    print(j)  # 0
    break

#0, 1, 2... 19, DONE!
k=0
while k < 20:
    print(k)
    k+=1
else:
    print('DONE!')

#while is very usefull in this case:
while True: 
    response = input("say something: ")
    if (response == 'bye'):
        break
