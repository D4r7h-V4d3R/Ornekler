### Birinci Yol
a = list(enumerate(["Istanbul","Ankara","İzmir","Bursa","Diyarbakır","Konya"]))
print(a)

### İkinci Yol
def enum(liste):
    boslis = []
    for i in range(len(liste)):
        boslis.append((i,liste[i]))
    return boslis
print(enum(["Istanbul","Ankara","İzmir","Bursa","Diyarbakır","Konya"]))

###Filter() Birinci yol
b = list(filter(lambda x : x % 2 == 0,[x for x in range(100)]))
print(b)

###filter() 2. Yol
c = [x for x in range(100) if x % 2 == 0]
print (c)