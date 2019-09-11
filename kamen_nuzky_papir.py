import random

mozne_tahy = ['kámen', 'nůžky', 'papír']

vyhry_pocitace = 0
vyhry_hrace = 0
tah_pocitace = random.choice(mozne_tahy)

#stejné
#hráč - počítač:
#kámen - nůžky Vyhrál
#kámen - papír Prohrál
#nůžky - papír Vyhrál
#nůžky - kámen Prohrál
#papír - kámen Vyhrál
#papír - nůžky Prohrál


while (vyhry_hrace != 3 and vyhry_pocitace != 3):
	tah_hrace = input("Zadej svůj tah (kámen, nůžky, papír): ")
	if tah_hrace in mozne_tahy:
		print("Tah počítače: " + tah_pocitace)
		if tah_hrace == tah_pocitace:
			tah_pocitace = random.choice(mozne_tahy)
			print("Znova, stejné tahy.")
		elif (tah_hrace == "kámen" and tah_pocitace == "nůžky") or (tah_hrace == "nůžky" and tah_pocitace == "papír") or (tah_hrace == "papír" and tah_pocitace == "kámen"):
			vyhry_hrace = vyhry_hrace + 1
			tah_pocitace = random.choice(mozne_tahy)
			print("Tohle kolo jsi vyhrál.")
			print(f'Skóre {vyhry_hrace} : {vyhry_pocitace}')
		elif (tah_hrace == "nůžky" and tah_pocitace == "kámen") or (tah_hrace == "papír" and tah_pocitace == "nůžky") or (tah_hrace == "kámen" and tah_pocitace == "papír"):
			vyhry_pocitace = vyhry_pocitace + 1 
			tah_pocitace = random.choice(mozne_tahy)
			print("Tohle kolo jsi prohrál.")
			print(f'Skóre {vyhry_hrace} : {vyhry_pocitace}')
	else:
		print("Asi ses překlikl, napiš to slovo správně a s diakritikou.")

if vyhry_hrace == 3:
	print("Třikrát jsi vyhrál, gratuluji. Skóre " + str(vyhry_hrace) + " : " + str(vyhry_pocitace))
elif vyhry_pocitace == 3:
	print("Smůla, počítač vyhrál, můžeš si zahrát ještě jednou. Skóre " + str(vyhry_pocitace) + " : " + str(vyhry_hrace))
