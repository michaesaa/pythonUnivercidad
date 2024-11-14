palabra = input("ingrese una palabrra").lower()
a = 0
e = 0
il = 0 
o = 0
u = 0

for i in range(len(palabra)):
    if palabra[i] =="a":
        a+=1
    if palabra[i] == "e":    
        e+=1
    if palabra[i] == "i":    
        il+=1
    if palabra[i] == "o":    
        o+=1    
    if palabra[i] == "a":    
        u+=1

print("a esta:",a)    
print("e esta:",e)    
print("e esta:",il)    
print("e esta:",o)    
print("e esta:",u)    
