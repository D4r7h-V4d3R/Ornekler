import re 

liste = ["özcan","özkan","özhan"
,"esra","esma",]

for isim in liste:
    obje = re.search("öz[kch]an",isim)#"es[rm]a"
    if obje:
        print(obje.group())