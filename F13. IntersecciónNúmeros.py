set1=[2, 4, 6, 8]
set2=[4, 5, 6, 9]
a={x for x in set1 if x % 2 == 0}
b={x for x in set2 if x % 2 == 0}
itc=a and b
print(itc)
