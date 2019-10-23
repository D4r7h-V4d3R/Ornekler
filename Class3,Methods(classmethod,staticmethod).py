class worke:
    zamoranı = 1.05
    def  __init__(self,ad,soyad,maas):#zam
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.mail = self.ad+self.soyad+"@corp.com"
    def fullname(self):
        return "Ad :{}, Soyad :{}".format(self.ad,self.soyad)
    def email(self):
        print(self.ad+self.soyad+"@corp.com")
    def zam(self):
        self.maas = (self.maas*self.zamoranı)
    
    @classmethod
    def zam_shift(cls,yoran):
        cls.zamoranı = yoran
worke.zam_shift(1.7)        
calıs1 = worke("Hasan","Kılıc",3100)
calıs2 = worke("Kemal","Ok",2300)
#farklı yontemler deniyelim
salıs3 = "Suleyman-Karagul-3900"
ad, soyad, maas = salıs3.split("-")
calıs3 = worke(ad,soyad,maas)
print(ad,soyad)
print(calıs1.maas)
calıs1.zam()
print(calıs1.maas)
print(calıs3.mail)