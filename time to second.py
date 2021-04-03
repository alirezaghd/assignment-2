
h = int(input('enter hours:\n'))
m = int(input('enter minutes: (must be between 0 to 59)\n'))
s = int(input('enter seconds: (must be between 0 to 59)\n'))
print('entered time is = ', str(h), ":", str(m), ':', str(s))
total_s = (h * 3600) + (m * 60) + s
print('total second is = ', str(total_s))
print('End.')