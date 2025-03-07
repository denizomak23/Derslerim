d = open("rehber.txt")
okunan = d.readlines()
print(okunan)
print(type(okunan))
for a in okunan:
    b = a.split("|")
    print(type(b))

