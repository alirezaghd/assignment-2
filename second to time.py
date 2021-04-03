
total_s = int(input('enter total second:\n'))
h = total_s // 3600
m = (total_s % 3600) // 60
s = (total_s % 3600) % 60
print('calculated time is = ', str(h), ':', str(m), ':', str(s))
