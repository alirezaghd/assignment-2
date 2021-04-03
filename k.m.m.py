


c = int(input())
d = int(input())

for i in range(d , c*d+1):
    if i % c == 0 and i % d == 0 :
        kmm = i
        break
print("K.M.M = ",kmm)



