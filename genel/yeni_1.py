
seç=int(input("Ortalama hesaplama için '1'   kalıp kalmadığınızı öğrenmek için '2'basın."))
if seç==2:
    notu=int(input("Notunuzu Girin:"))
    if notu==150 :print("sınırdasın yazıklar olsun anca geçtin")
    elif notu<50:print("laf yok gerçekten birşeyler söyleyemiyorum KALDIN")
    elif notu>90:print("vaay parlak bir zeka tebrik ederim")
    exit()

if seç==1:
    n1=int(input("ilk dönem not girin:"))
    n2=int(input("2. dönem not girin"))
    if n1>100 or n2>100 or n1<0 or n2<0: print("geçersiz not girişi")

ortalama = (n1+n2)//2
print(ortalama)


