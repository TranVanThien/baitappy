a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b :
    if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b :
      print ("day la tam giac vuong")
    else :
     print("day la ba canh cua 1 tam giac")
else:
    print("ba canh do khong tao thanh 1 tam giac")
