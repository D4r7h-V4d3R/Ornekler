#Yol bir
def uc(liste):
    yeliste = [i for i in liste if i%3==0]
    return yeliste
sayilar=[3,4,5,7,8,9,0,7,5,3,2]
print(uc(sayilar))

#Yol İki
sayilar=[3,4,5,7,8,9,0,7,5,3,2]
print(list(filter(lambda x : x %3==0 ,sayilar)))
#Harf ornegi ile
rehber = ["ali","adam","malik","jason"]
print(list(filter(lambda x: "m" in x ,rehber)))