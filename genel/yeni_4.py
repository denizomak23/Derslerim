def hmmenu():
    print("\033[1;32;40m")
    
    
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   HM MENU  \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Topla            ║")
    print("║  2-Çarp             ║")
    print("║  3-...              ║")
    print("║  4-                 ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    s1 = int(input("1.sayı nedir:"))
    s2 = int(input("2.sayı nedir:"))
    def topla(a,b):
        return a+b
    def carp(a,b):
        return a*b
    if secim == "1" : print(topla(s1,s2))
    if secim == "2" : print(carp(s1,s2))
   
def oyunlar():
    print("Bu menu henüz hazır değil")
def anamenu():
    print("\033[1;32;40m")
    
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   VEKTOREL APP  \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Oyunlar          ║")
    print("║  2-Hesp mak.        ║")
    print("║  3-                 ║")
    print("║  4-                 ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1" : oyunlar()
    if secim == "2" : hmmenu()
    if secim == "9" : exit()
    else : anamenu()
anamenu()