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
    def __repr__(self):
        return "calısan ('{}','{}','{}')".format(self.ad,self.soyad,self.maas)
    def __str__(self):
        return "{} , Email :{}".format(self.fullname(),self.mail)     
    def __add__(self,other):
        return self.maas + other.maas
calıs1 = worke("Hasan","Kılıc",3100)
calıs2 = worke("Kemal","Ok",2300)

#print(5+9)
#print("ali"+"veli")
print(int.__add__(5,9))
print(str.__add__("ali","veli"))

print(calıs1)
print(repr(calıs1))
print(str(calıs2))
print(calıs2.__str__())
print(calıs1+calıs2)