#Birinci Yol(define ile)

def kare(x):
    # y = x**2
    return x**2 #y
print(kare(2))

#İkinci Yol(with lambda)

lamba = lambda x : x**2
print(lamba(2))

#Biraz ornek

or1 = lambda x ,y: x if x>y else y 
print(or1(3,9))

or1 = lambda s,z: s**z
print(or1(3,45))
