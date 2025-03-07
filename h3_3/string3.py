abc = "ErDiNç DöNmez" # string (metin türü) bir değişken tanımladık
print ("erDiNç".capitalize()) # İlk harf büyük
print("ErDiNç".lower()) # küçük harfe çevir
print("ErDiNç".upper()) # büyük harfe çevir
print(abc.swapcase()) # Büyük küçük harfleri değiştir.
print(abc.title()) # Kelimelerin ilk harflerini büyüt
print(abc.replace("E","a")) # “E” leri “a” yap
print(abc.upper().replace("E","a")) # Önce büyük harfe çevir, sonra “E” leri “a” yap
print(abc.count("D")) # Metindeki bazı karakteler veya karakter gruplarının sayısı
print(abc.find("Dö")) # “Dö” ifadesi kaçıncı indexte 

