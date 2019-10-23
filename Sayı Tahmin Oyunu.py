
import random
import time
import oyun

def tahmin():
    sayi_tahmin =int(input("Tahmini Sayınız :"))
    return sayi_tahmin

def Basla():
    print ("\n******//Sayı Tahimin Oyununa Hoşgeldiniz\\\*******\n")
    
    sayac = 0
    
    makine_random = random.randint(0,101)
    while True:
        tahminen = tahmin()
        if tahminen > makine_random:
            print ("Kontrol Ediliyor.",end="")
            for i in range(3):
                time.sleep(1)
                print(".",end="",sep="")
            print("Girdiğniz Sayı Büyük !")
        elif tahminen < makine_random:
            print ("Kontrol Ediliyor.",end="")
            for i in range(3):
                time.sleep(1)
                print(".",end="",sep="")
            print("Girdiğniz Sayı Küçük !")
            
        elif tahminen == makine_random:
               time.sleep(1)
               print(".",end="",sep="")
               print("\n   Tebrikler Doğru..")
               print("{} Denemede Buldunuz.".format(sayac))
               break
        sayac += 1

Basla()
        
            
        
                
            