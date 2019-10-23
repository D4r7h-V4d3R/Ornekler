#burada bazı teknikleri anlatıyorum..
class worke:
    zamoranı = 1.05
    def  __init__(self,ad,soyad,maas):#zam
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.mail = self.ad+self.soyad+"@corp.com"
        #yada burada zam yapalım
        #self.zam = self.maas*self.zamoranı
    def fullname(self):
        return "Ad :{}, Soyad :{}".format(self.ad,self.soyad)
    def email(self):
        print(self.ad+self.soyad+"@corp.com")
    def zam(self):
        self.maas = (self.maas*calıs1.zamoranı)
        
        
calıs1 = worke("Hasan","Kılıc",3100)
calıs2 = worke("Kemal","Ok",2300)
print(calıs1.ad,calıs1.soyad)
print(calıs1.fullname())
print(calıs2.mail)
print(calıs1.maas)
calıs1.zam()
print(calıs1.maas)
