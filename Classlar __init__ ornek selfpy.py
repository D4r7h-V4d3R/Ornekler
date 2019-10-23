# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:58:33 2019

@author: Nob0dY
"""

class Sirket():
    def __init__(self,çalışans,şirketi,boss,yatırımcılar,aktivasyon):
        self.çalışans = çalışans
        self.şirketi = şirketi
        self.boss = boss
        self.yatırımcılar = yatırımcılar
        self.aktivasyon = aktivasyon
        
    def çalisanAl(self,sayi):
        self.çalışan  += sayi
        
    def çalisanKov(self,sayi):
        self.çalışan  -= sayi    
        
    def şirketis(self,isim):
        self.şirketi = isim
        
    def bossAdd(self,isim):
        self.boss.append(isim)
        
    def yatırıcıEkl(self,isim):
        self.yatırımcılar.append(isim)
        
    def Batır(self):
        self.aktivasyon = False

    def Arsiv(self):
        print("""
              Şirket İsmi = {}
              Çalışan Sayısı = {}
              Mudurs = {}
              Yatırımcılar {}
              Aktivasyon = {}
              """.format(self.şirketi,self.çalışans,self.boss,self.yatırımcılar,self.aktivasyon))
        
        test = Sirket(70,"Test",["overflougs,blacky"],["Chucky,Black Rose"],True)
        test.Arsiv()
        
        