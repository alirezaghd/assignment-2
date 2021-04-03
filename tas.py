import random
while True:
    t = random.randint(1, 6)
    if t == 6:
        print('tas is 6 and you have another chance')
        print('----------------')
    else:
        print('tas is not 6 and end of your chance')
        break
print('End.')
