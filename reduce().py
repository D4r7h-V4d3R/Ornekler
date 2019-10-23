from functools import reduce

#Bir Listenin en Büyük elemanını bulmak
#Birinci Yol

liste = [1,2,32,54,3,63,74,2,45,24,62,4]
print(max(liste))

#İkinci Yol 
q = lambda a,b: a if (a>b) else b
print(reduce(q,liste))

#Bence bir yolu daha var X)

yenil = []
for i in liste:
    if i >50:
        yenil.append(i)
print(yenil)
#Ve daha niceleri...
#Biraz daha reduce() ornekliyelim.hmm faktoriyel..
calc = lambda x , y: x*y
print(reduce(calc,[1,2,3,4,5,6,7,8,9]))
#yazmaya usenenler ıcın --.
#print(reduce(calc ,[x for x in range(1,10)])) #1 dahil 10 haric
