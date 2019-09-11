from random import randint
from util import tah

def tah_pocitace(pole,symbol):
	"""Vrátí herní pole se zaznamenaným náhodným tahem počítače. 
	"""
	if "-" not in pole:
		raise ValueError("Došla volná pole.")
	#while True:
	if symbol == "o":
		if "o-o" in pole: 
			pozice_p = pole.index("o-o") + 1
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "x-x" in pole:
			pozice_p = pole.index("x-x") + 1
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "-oo" in pole: 
			pozice_p = pole.index("-oo") 
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "oo-" in pole: 
			pozice_p = pole.index("oo-") + 2
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "xx-" in pole:
			pozice_hrace = pole.index("xx-")
			pozice_p = pozice_hrace + 2
			print(pozice_p)
			return tah(pole,pozice_p,symbol)
			
		elif "-xx" in pole:
			pozice_p = pole.index("-xx")
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "-x-" not in pole:
			if "-o" in pole:
				pozice_p = pole.index("-o")
				print(pozice_p)
				return tah(pole,pozice_p,symbol)
			elif "o-" in pole:
				pozice_p = pole.index("o-") + 1
				print(pozice_p)
				return tah(pole,pozice_p,symbol)

		elif "-x" in pole:
			pozice_p = pole.index("-x")
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "x-" in pole:
			pozice_p = pole.index("x-") + 1
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

	if symbol == "x":
		if "x-x" in pole: 
			pozice_p = pole.index("x-x") +1
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "o-o" in pole:
			pozice_p = pole.index("o-o") + 1
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "-xx" in pole: 
			pozice_p = pole.index("-xx") 
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "xx-" in pole: 
			pozice_p = pole.index("xx-") + 2
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "oo-" in pole:
			pozice_hrace = pole.index("oo-")
			pozice_p = pozice_hrace + 2
			print(pozice_p)
			return tah(pole,pozice_p,symbol)
			
		elif "-oo" in pole:
			pozice_p = pole.index("-oo")
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "-o-" not in pole:
			if "-x" in pole:
				pozice_p = pole.index("-x")
				print(pozice_p)
				return tah(pole,pozice_p,symbol)
			if "x-" in pole:
				pozice_p = pole.index("x-") + 1
				print(pozice_p)
				return tah(pole,pozice_p,symbol)

		elif "-o" in pole:
			pozice_p = pole.index("-o")
			print(pozice_p)
			return tah(pole,pozice_p,symbol)

		elif "o-" in pole:
			pozice_p = pole.index("o-") + 1
			print(pozice_p)
			return tah(pole,pozice_p,symbol)
						
	pozice_p = randint(0,19)
	while pole[pozice_p] != "-":
		pozice_p = randint(0,19)
		print(pozice_p)
	return tah(pole,pozice_p,symbol)













