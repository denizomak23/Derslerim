aa = "Vektörel"

for x in range(len(aa)+1):
	print(aa[:x]," "*(len(aa)+1-x),"",""*(len(aa)+1-x),aa[:x])

for x in range(len(aa)+1):
	print(aa[:x],""**(len(aa)+1-x),"",""*(len(aa)+1-x),aa[:x])


    