#normal OOP Programmlama tarzı (basit programlama)
#uninit un self
class work:
    pass
emplo1 = work()
emplo1.ad = "Hasan"
emplo1.soyad = "Kılıc"
emplo1.maas = "3100"

emplo2 = work()
emplo2.ad = "Kemal"
emplo2.soyad = "Ok"
emplo2.maas = "2300"

print(emplo1)
print(emplo1.ad,emplo1.soyad)

#With init,self;
#su anki kesfime gore __init__ kullanıca calısanın bilgilerine sadece calıs. deyince ulasılabilir
#ama def fonksiyonu sorun cıkarmaya daha yatkındır calıs.fullname() diye __init__ de ise calıs.fullname 
#denilmesi yeterlidir..
class worke:
    def  __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.mail = self.ad+self.soyad+"@corp.com"
    def fullname(self):
        return "Ad :{}, Soyad :{}".format(self.ad,self.soyad)
    def email():
        print(self.ad+self.soyad+"@corp.com")
calıs1 = worke("Hasan","Kılıc",3100)
calıs2 = worke("Kemal","Ok",2300)
print(calıs1)
print(calıs1.ad,calıs1.soyad)
print(calıs1.fullname())
print(calıs2.mail)
print(calıs1.mail)

#hold to line