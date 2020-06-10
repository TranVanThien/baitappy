import math
a = int(input())
b = int(input())
c = int(input())
s = b**2 - 4*a*c
if s < 0 or a == 0  :
   print('pt vo nghiem')
elif s > 0:
    print('pt co 2 nghiem phan biet x1= ',( -b+math.sqrt(s) ) / (2*a), " x2 = ", ( -b-math.sqrt(s) ) / (2*a))
else :
    print('pt co nghiem kep x1 = x2 = ', -b/(2*a))


