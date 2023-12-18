# https://codeforces.com/problemset/problem/546/A 
(k, n, w) = tuple(map(lambda x: int(x) if x != '' else None, input().split(" ")))
print((lambda x: 0 if x <= 0 else x)(k*w*(w+1)//2-n))
#1) (k, w, n) - скобки не нужны, визуальное представлние. Более подробно https://habr.com/ru/articles/499666/
#2) input().split(" ") - подаются в ряд числа разделенные пробелом. split(" ")- их разделяет.
# Но можно просто split(), тк пробел внутри стоит по дефолту
# 3) lambda x: int(x) if x != '' else None
#преобразуем число типа str в int  спомощь. lambda

# 4) lambda x: 0 if x <= 0 else x
# если x отрицателтное или 0, то превращаем его в 0(избавляемся от отриц чисел),
# если положительно, то так его и оставляем

#link: https://codeforces.com/problemset/problem/450/A
#solve1 
n, m = map(int, input().split())
li = tuple(map(int, input().split()))
li_temp = list(li)
li1 = []
temp = list(li)
for i in range(n):
    if li_temp[i]-m < 0:
        li_temp[i] = 0
    else:
        li_temp[i] -= m
# print(li_temp)
if li_temp.count(0) == len(li_temp): # что здесь происходит?
    print(n)
else:
    while True:
        for i in range(n):
            li1.append(temp[i]-m) if temp[i] - m > 0 else li1.append(0)
        # print(li1)
        # print(temp)
        if li1.count(0) == len(li1):
            for k in range(len(temp)-1, -1, -1):
                if temp[k] != 0:
                    temp1 = k
                    break
            break
        else:
            temp = li1
            li1 = []
    print(temp1+1)

#solve2
    n, m = map(int, input().split())
zz = list(map(int, input().split()))
mx = -10**10
for i in range(len(zz)):
    a = zz[i]
    if (a + m - 1) // m >= mx:
      p = i + 1
      mx = (a + m - 1) // m
print(p)

#solve3
n,p=map(int,input().split())
a=list((int(i)-1)//p for i in input().split())
print(n-a[::-1].index(max(a)))
    


















 