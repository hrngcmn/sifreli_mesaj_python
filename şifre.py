liste1=[]
liste2=[]
liste3=[]
a = input("Sifrelemek istediğiniz mesajı giriniz: ")
for i in a:
    liste1.append(ord(i))
#print(liste1)
for k in liste1:
    liste2.append(k + 2)
#print(liste2)
for n in liste2:
    liste3.append(chr(n))
print("Şifrelenmiş Mesajınız:",end="")
for m in liste3:
    print(m,end="")
print("")
#............
# Bu mesajı alacak kişinin çözmesi için gerekli kodlar alt tarafta yazılmıştır.
#............
liste4= []
liste5 =[]
b = input("Çözülecek mesajı giriniz: ")
for i in b:
    liste4.append(ord(i)-2)
#print(liste4)
for k in liste4:
    liste5.append((chr(k)))
#print(liste5)
for n in liste5:
    print(n,end="")

