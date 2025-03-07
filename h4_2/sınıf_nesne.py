class Ilan():
    ilan_no = "----"
    ilan_adi = "----"
    ilan_aciklamasi = "Açıklama girilmedi"

    def __init__(self, a, b, c):
        self.ilan_no = a
        self.ilan_adi = b
        self.ilan_aciklamasi = c

    def ilan_bilgileri(self, uyelik_tipi):
        if uyelik_tipi == "premium":
            print("Merhaba çok değerli üyemiz.")
            print(f"İlan adı: {self.ilan_adi}, İlan no: {self.ilan_no}, İlan açıklaması: {self.ilan_aciklamasi}")

        if uyelik_tipi == "basic":
            print("Merhaba değerli üyemiz.")
            print(f"İlan adı: {self.ilan_adi}, İlan no: {self.ilan_no}")

ilan_2341 = Ilan("257", "On numara şahin", "Temiz, 210 binde, ...")
ilan_5784 = Ilan("874", "Kiralık ev", "3+1 metroya yakın, kombili, ...")

ilan_2341.ilan_bilgileri("premium")
ilan_2341.ilan_bilgileri("basic")