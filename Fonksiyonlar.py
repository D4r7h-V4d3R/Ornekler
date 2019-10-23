#upper() fonksiyonu
a = "Bitcoin 2009'da Piyasaya sürüldü"
print(a.upper())
#BITCOIN 2009'DA PIYASAYA SÜRÜLDÜ

#lower() fonksiyonu
print(a.lower())
#bitcoin 2009'da piyasaya sürüldü

#replace() fonksiyonu
print(a.replace("0","O"))
#Bitcoin 2OO9'da Piyasaya sürüldü

#startswith() fonksiyonu
print(a.startswith("Bitcoin"))
#True
##print(a.startswith("coin"))
#False
###endswith() fonksiyonu
print(a.endswith("üldü"))
#True

###.join() fonksiyonu
liste = ["Our","Democrasy","Has been ","Hacked!"]
print(" ".join(liste))
#Our Democrasy Has been  Hacked!

###.count () fonksiyonu
listx = "Our Democrasy Has been Hacked!"
print(listx.count("e"))
#4

###.find() fonksiyonu
print(listx.find("r"))
###.count() belirtilen karekterin kaç kere geçtiğini bildirir
###.find() ise kaçıncı index olduğunu bildirir
##print(listx.rfind("r"))
#9


###strip() fonksiyonu
nick = "000000000000000000000x000gandalf000000000000000000000"
print(nick.strip("0"))
#x000gandalf
##print(nick.lstrip("0"))
#000000000000000000000x000gandalf
##print(nick.rstrip("0"))
#x000gandalf000000000000000000000

###split() fonksiyonu
print(a.split(" "))
#['Bitcoin', "2009'da", 'Piyasaya', 'sürüldü']
###Attention This is a Example for split()
langs = input("En sevdiğiniz prog. dillerini giriniz :")
lista = langs.split(",")
print(lista)