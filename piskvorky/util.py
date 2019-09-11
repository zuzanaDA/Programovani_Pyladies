
def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici
    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka."""
    if pozice >= len(pole): # not in range(0,20):
    	raise ValueError("Zadej pozici uvnitř hracího pole.")
    elif pozice < 0:
        raise ValueError("Zadej pozici uvnitř hracího pole.")
    elif pole[pozice] != "-":
    	raise ValueError('Pozice je již obsazena.')
    elif symbol not in ("x", "o"):
    	raise ValueError('Symbol musí být "x" nebo "o".')
    else:
    	return pole[:pozice] + symbol + pole[pozice+1:]


