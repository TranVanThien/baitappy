while True:
    n = int(input('nhap 1 so duong = '))
    if n > 0:
        break
if n < 10:
    print (n, ' la tong cac chu so cua so ',n)
else :
    s = 0;
    while n != 0:
        s += n % 10
        n= int(n/10)
print(s)