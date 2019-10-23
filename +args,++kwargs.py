#Normalde Yapılanlar
#Not:illede adı args veya kwargs olmak zorunda degil 
#onemli olan basında yıldızı(*) olmasıdı ornegin *arguman veya **keyarm da olabilir isim degiskendir..
m1 = "Abrham Tank"
m2 = "T34"
m3 = "PANZER Tiger"
m4 = "M4A1 Glock with 14mm"
heat = "Military"

def forces(heat,a,b,c,d):
    print("Head : " + heat)
    print(a)
    print(b)
    print(c)
    print(d)

forces(heat,m1,m2,m3,m4)#m5,m6,m7 Girilirse HATA VERİR

#Yani Burada yapılanlar uzun ve gereksiz kod kalabalıgından ibaret
#Her biri 2 kere tanıtılmıs 3 kere girilmis so böyle durumlarda kullancıgımız arkadasa gecelim

#*args ,**kwargs (arhumanlar,keyworldargumanlar)
#arguman ornegi
print("\n\n------------------------\n\n")
def forses(heat,*args):#heat demek onu ayrı tutar yoksa sadece(*args) denilebilir
    print(heat)
    for i in args:
        print(i)
forces(heat,m1,m2,m3,m4)#,3,6,9,"suleyman",3.53 gibi istenildigi kadar arguman girile bilir
#ve bunlar tanıtma gerektirmez..

#Listeden *argumana ceviriler;
def fors(heat,*args):
    print(heat)
    for i in args:
        print(i)
meta =["meta1","meta2","meta3"]
fors(heat,meta)#Farka iyi bak
fors(heat,*meta)

#kwargs lara gecelim

bas = "Programming langs"
def orkwargs(heat,*args,**kwargs):
    print("Konu : " + bas)
    for i in args:
        print(i)
    for i in kwargs.items():
        print(i)
orkwargs(bas ,
         metin = "merhaba",
         metin1 = "hello",
         metin2 = "konnichiwa")

