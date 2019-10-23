#not:
#Public = self.bronzm =bronz demek sporcu.bronz denerek erısilebilir
#Protected(yarı gizli) = self._gumusm = gumus demek sporcu._gumus
#Secret (sır,gizli) = şimdi burada iş degişir ,bunlara dogrudan erişim İmkansızdıR.. ancak verileri okunabilir şoyle:
#amadalya =self.__altinm 
#print( "ALTIN : {}".format(amadalya))
##yani type degistirecegiz altın = self.__altinm
##print(altin)
class sporcu():
    def __init__(self,ad,brans,altin,gumus,bronz):
        self.ad = ad
        self.brans = brans
        self.bronzm =bronz #Public Veri(Halka Acık)
        self._gumusm = gumus #_semi public,protected(yarı gizli)
        self.__altinm = altin #__Top Secret (private tam gizli)
    #@property
    def apr(self):
        amadalya =self.__altinm #yada daha profesyonel yontem olan;
        #return "ALTIN : {}".format(amadalya)
        print( "ALTIN : {}".format(amadalya))
    def atlet_information(self):
        return "Ad : {} \nBrans : {} ".format(atlet1.ad,atlet1.brans)
atlet1 = sporcu("hakan","100 metre",2,4,8)
print(atlet1.atlet_information())
print("bronz :",atlet1.bronzm)
print("Gumus :",atlet1._gumusm)
atlet1.apr()