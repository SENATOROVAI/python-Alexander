# https://codeforces.com/problemset/problem/546/A 
(k, n, w) = tuple(map(lambda x: int(x) if x != '' else None, input().split(" ")))
print((lambda x: 0 if x <= 0 else x)(k*w*(w+1)//2-n))
#1) (k, w, n) - скобки не нужны, визуальное представлние. Более подробно https://habr.com/ru/articles/499666/
#2) 

