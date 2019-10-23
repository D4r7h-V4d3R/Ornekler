#hadi baslayalım here we go..
###min ,max 1
points = [2700,2560,2100,1950]
print(min(points))
print(max(points))

###min ,max 2

points = [2700,2560,2100,1950]
short = points.sort(reverse=True)#or False
print(short)

###Birinci Yol
teams = ["SauerCloud","PPP","Ninjas","TokyoWesterns"]
points = [2700,2560,2100,1950]
print(list(zip(teams,points)))

###İkinci yol
def esle (liste1,liste2):
    liste = []
    for los in range(len(liste1)):
        liste.append((liste1[los],liste2[los]))
    return liste
teams = ["SauerCloud","PPP","Ninjas","TokyoWesterns"]
points = [2700,2560,2100,1950]
print(esle(teams,points))