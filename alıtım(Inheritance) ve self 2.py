# -*- coding: utf-8 -*-
#evet yaptıgımız ornekler ile kalıtım..
class work():
    def __init__(self,maas,isim,yas):
        self.maas = maas
        self.isim = isim
        self.yas = yas
        
    def goster(self):
        print("İsim : {} \n Yas = {} \n Maas {}".format(self.isim,self.yas,self.maas))
        
        
        
        
class manager(work):
    def __init__(self,maas,isim,yas,etki):
        super().__init__(maas,isim,yas)
        self.etki = etki
        
    def goster(self):
        print(" İsim : {} \n Yas = {} \n Maas :{} \n Etki ={}".format(self.isim,self.yas,self.maas,self.etki))
    
y1 = manager("Testy",33,3000,True)
y1.goster()
        