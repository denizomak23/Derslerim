import re
metin1 = "bugün hava çok soğuk"
metin2 = "bugün hava çok sıcak"
metin3 = "bugün hava soğuk"
metin4 = "çok güzel bir hava var"

aranan= "çok"

print(re.search(aranan, metin4))