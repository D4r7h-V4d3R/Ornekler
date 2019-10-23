class worke():
    zamoranı = 1.05
    def  __init__(self,ad,soyad,):
        self.ad = ad
        self.soyad = soyad

    @property
    def mail(self):
        self.email = self.ad + self.soyad + "@corp.com"
        return self.email

    def fullname(self):
        return "Ad :{}, Soyad :{}".format(self.ad,self.soyad)
 
    @fullname.setter
    def fullname(self,inconame):
        ad ,soyad = inconame.splite("")
        self.ad = ad
        self.soyad = soyad
calıs1 = worke("Hasan","Kılıc")
calıs1.ad = "Ali"
#Takalım fise ve deniyelim
print(calıs1.fullname())
# Output;
#Ali
#HasanKılıc@corp.com
#Ad :Ali, Soyad :Kılıc

#hmm buna ragmen email degismedi 
#farklı bir yontem deneyelim
#line;7
#Yani uzun lafın kısası (bulgularımca)
#sadece print(calıs1.mail()) diyecegimize
#print(calıs1.mail) diyebiliyoruz yani varsayımsal olarak
#onuda __init__ in icine ekliyor ve hatta __init__ e tanıtılması bile gerekmiyor...
#liste = [1,2,3,4,5,6,7,8,9,0]
#for i in liste:
#    print(i)
#while True:
#    print(liste)
#    break
#

print(calıs1.mail)
