#Birinci Yol
def ikiye(katlan):
    katlanm=[]
    for i in katlan:
        katlanm.append(i*2)
    return katlanm
liste=[3,6,9,13]
print(ikiye(liste))

#İkinci Yol (map)
lista = [1,2,3,4,5,6,7]
print(list(map(lambda x :x**2 ,lista)))

keyboards = [("logitech",75),("razer",240),("MSI",140)]
ucuz_mu = lambda dizi:(dizi[0],"Ucuz" if dizi[1]<150 else "Yok bee pahalı")
print(list(map(ucuz_mu,keyboards)))