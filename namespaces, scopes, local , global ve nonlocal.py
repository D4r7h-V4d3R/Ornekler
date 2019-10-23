# neyin ne oldugu python ın nasıl calıstıgını anlatıyorum

a = 1
print("id(1) = " , id(1))
print("id(a) = ", id(a))
#Output =
#id(1) =  140715885957952
#id(a) =  140715885957952

#>_Tamam mantıken a = 1 olur ancak
#mantıksal bir islemde nasıl yürur?
#>_c

print("id(a) = " ,id(a),id(1))
a = a+1
print("id(a) = ", id(a))
print("id(3) =",id(3))
b = 2
print("id(2) = " ,id(2),id(b))

def printhello():
    print("hello")
a = printhello()
#bir fonksiyon ve  aynı zamannda nesne oldugunun kanıtı
print("id(a,(printhello)) = ",id(a))

def dis():
    b = 20
    def ic():
        c = 30
a = 10
print(a)#,b Error "b" is not defined

def dıss():
    s = 20
    def icc():
        s = 30
        print("s = " ,s)
    icc()
    print("s = ",s)
s = 10
print("s = " ,s)
dıss()
print("---------------")


def dis():
    global z 
    print(z)
    z = 20
    print(z)
    def ıc():
        global z 
        z = 30
        print("z = ",z)
    ıc()
    print("z = ",z)
z = 10
dis()

print("---------------------")
def test():
    def locall():
        indx = "lokal index"
    def non_local():
        nonlocal indx
        indx = "no lokal index"
    def globall():
        global indx
        indx = "global index"
    indx = "index deneme"
    locall()
    print("lokallestirildikten sora =",indx)
    non_local()
    print("nonlokallestirildikten sora =",indx)
    globall()
    print("globallestirildikten sora =" ,indx)
test() 
print("global kasif",indx)