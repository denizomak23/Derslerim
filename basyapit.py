
print("Merhaba, sitemize hoş geldiniz siteyi sadece yetişkinler kullanabilir")
ist1=input("Eğer yetişkinseniz '1' yazın değilse '2' yazın:")
if ist1 == "1":print("merhaba yetişkin olduğunuzu kabul ettiniz giriş yapın lütfen")
elif ist1 == "2":print("yetişkin olmadığınızı belirttiniz dürüstlük için teşekkürler")
if ist1 =="2":exit()
print("\n")
print("⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤")
isim=input("⎢İsminiz Nedir:")
soyisim=input("⎢soyisminiz nedir:")
print(f"⎟Hoşgeldin,{isim}\t{soyisim}")
dy=int(input(f"⎮{isim}\t{soyisim}\tdoğum yılınız nedir:"))
if dy > 2007:print("sisteme giremezsin yaşın 18 den küçük")
else:print(f"⎢yaşın: {(2025-dy)} sisteme hoşgeldiniz")



