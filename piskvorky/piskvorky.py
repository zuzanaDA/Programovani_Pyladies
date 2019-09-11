from util import tah
from ai import tah_pocitace

def vyhodnot(retezec):
	"""dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry"""
	if "xxx" in retezec:
		return "x"
	elif "ooo" in retezec:
		return "o"
	elif "-" not in retezec:
		return "!"
	else:
		return "-"

def tah_hrace(pole,symbol):
	"""Zeptá se hráče na tah a vrátí nové herní pole"""
	while True:
		pozice = input("Kam chceš hrát? (0-19) ")
		try:
			pozice = int(pozice)
		except ValueError:
			print("Napiš číslo.")
		else:
			try:
				return tah(pole, pozice, symbol)
			except ValueError:
				print("tam nejde hrát")

def piskvorky1D(): 
	"""vytvoří první řetězec s dvaceti pomlčkami 
	a nastřídačku bude volat funkce tah_hrace a tah_pocitace 
	a vypisovat stav hry
	Závěr hry se vyhodnotí podle funkce vyhodnot"""
	pole = 20 * "-"
	symbol = input('Chceš hrát za křížky ("x") nebo za kolečka ("o")? ')

	while symbol not in ("x","o"):
		symbol = input('Povolené znaky jsou jen křížky ("x") nebo za kolečka ("o"): ')

	if symbol == "x":
		symbol_pocitace = "o"
	elif symbol == "o":
		symbol_pocitace = "x"

	while True:
		if vyhodnot(pole) == "!":
			return print("Došla pole, remíza!")
		else:
			
			pole = tah_hrace(pole, symbol)
			if vyhodnot(pole) == symbol:
				print(pole)
				return print("Vyhrál jsi!")
			if vyhodnot(pole) == symbol_pocitace:
				print(pole)
				return print("Vyhrál počítač!")
			else:
				print(pole)

			pole = tah_pocitace(pole, symbol_pocitace)
			if vyhodnot(pole) == symbol:
				print(pole)
				return print("Vyhrál jsi!")
			if vyhodnot(pole) == symbol_pocitace:
				print(pole)
				return print("Vyhrál počítač!")
			else:
				print(pole)




