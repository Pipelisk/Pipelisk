Personajes=["Obi-Wan Kenobi", "Plo Koon", "Mace Windu", "Yoda", "Maul", "Sidious", "Malgus", "Vader","Boba Fett","Bossk","Din Djarin"]

Jedis=["Obi-Wan Kenobi","Plo Koon","Mace Windu", "Yoda"]

Siths_Lords=[]

Siths=["Maul","Sidious","Malgus","Vader"]

Caza_Recompensas=["Boba Fett","Bossk","Din Djarin"]

def caeralladooscuro():
	for i in range(3):
		Siths_Lords.append(("Darth ")+Siths[i])

def imprimir_nombres():
	for i in range(len(Personajes)):
		print(Personajes[i])

print("Personajes")
imprimir_nombres()
caeralladooscuro()

print("")
print("Señores Oscuros")
for i in range(len(Siths_Lords)):
	print(Siths_Lords[i])
print("")
print("Jedis")
for i in range(len(Jedis)):
	print(Jedis[i])
print("")
print("Caza Recompensas")
for i in range(len(Caza_Recompensas)):
	print(Caza_Recompensas[i])