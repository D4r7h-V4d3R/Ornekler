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

class developer(worke):
   def __init__(self,ad,soyad,maas,plang):
       #worke.__init__(self,ad,soyad,maas,plang)
       super().__init__(ad,soyad,maas)
       self.plang=plang
       self.zamoranı=1.3
class manager(worke):
   def __init__(self,ad,soyad,maas,workers = None):
       super().__init__(ad,soyad,maas)
       if workers is None:
           self.workers = []
       else:
           self.workers=workers
   def add_worker(self,calısan):
       self.workers.append(calısan)
   def remove_worker(self,calısan):
       self.workers.remove(calısan)
   def worker_display(self):
        for i in self.workers:
            print(i.fullname)


calıs2 = worke("Kemal","Ok",2300)
#farklı yontemler deniyelim
salıs3 = "Suleyman-Karagul-3900"
ad, soyad, maas = salıs3.split("-")
calıs3 = worke(ad,soyad,maas)
dev1 = developer("cengiz","tura",3900,"Bash-sh")
man1= manager("Hamza","Beyazgul",4000,[dev1,calıs2])
print(dev1.fullname())
dev1.zam()
print(dev1.maas)
man1.add_worker(dev1)
print(man1.worker_display())
print(isinstance(calıs2,manager))
print(issubclass(developer,worke))