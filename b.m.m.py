


a = int(input())
b = int(input())

for i in range(a , b+1):
    if a % i == 0 and b % i == 0 :
        bmm = i
        break
print("B.M.M = ",bmm)



