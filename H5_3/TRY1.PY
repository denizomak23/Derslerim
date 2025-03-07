print("Bölme İşlemi")

try:
    a = input("bölünecek sayıo nedir ?")
    b = input("bölecek sayı nedir?")
    a = int(a)
    b = int(b)
    print(a/b)


except ValueError:
    print("yanlış değer girdiniz")

except ZeroDivisionError as h:
    print("sıfıra bölüm hatası.",h)

except Exception as hata:
    print("bir hata oluştu:", hata)

else: pass

finally:
    print("işlem bitti")