s = str(input())
max = s[0]
min = s[0]
for i in range(1,len(s)):
    if max < s[i]:
        max = s[i]
    if min > s[i]:
        min = s[i]
print (max,' ',min)