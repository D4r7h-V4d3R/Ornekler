from functools import reduce
#reduce bir çoklu işlem aracıdır
a = reduce(lambda a,b : a+b,[12,34,56,78])
print (a)

ls = [12,34,56,78]
for i,s in ls:
    print(i+s)