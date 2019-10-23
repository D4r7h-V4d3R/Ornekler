# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:21:37 2019

@author: Nob0dY
"""
#liste işlemleri ve yolları
# way 1=
print ("***********************************************************")
print ("***********************************************************")

lif = []

for dl in range(0,101,2):
   if dl % 2 is 0 :
        lif.append(dl)
    
print(lif)

#way 2 =
print ("***********************************************************")
print ("***********************************************************")

for way2 in range(0,101,2):
    print(way2)
    

#way 3 =
print ("***********************************************************")
print ("***********************************************************")
    
    
liste = [i for i in range(0,101) if i % 2 == 0]
print(liste)

#List Comprehension 1 =
print ("***********************************************************")
print ("***********************************************************")
tuple_list = [(1,2),(3,4),(5,6),(7,8),(9,0)]

wtf = [a*x for a,x in tuple_list]
print (wtf)



litse = [[1,3,5,7,9],[13,337,1337],[3,7,40]]
for bir in litse:
    print("this is one\n")
    for iki in bir:
        print("this is two\n")

        print(iki)
        
#List Comprehension 2 =

List_Comprehension  = [[1,2,3,4,5,6,7,8,9],[10,20,30,40,50,60,70,80,90],[11,22,33,44,55,66,77,88,99]]

real_List_Comprehension  = [x for i in List_Comprehension for x in i]
print (real_List_Comprehension)



        
        