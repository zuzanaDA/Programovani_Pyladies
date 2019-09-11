from random import randint, choice

def obrazek(level):
    if level == 0:
        return ""
    elif level == 1:
        return """
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 2:
        return """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 3:
        return """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 4:
        return """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        """
    elif level == 5:
        return """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        """
    elif level == 6:
        return """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        """
    elif level == 7:
        return """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        """
    elif level == 8:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        """
    else:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~
        """

def nahodne_slovo():
    """vybere náhodné slovo ze seznamu slov"""
    seznam_slov = ["ananas","kočka","rejsek","stromeček"]
    nahodne_slovo = choice(seznam_slov)
    return nahodne_slovo

def zamen(nahodne_slovo, pole, pismeno):
    """zamění podtržítko za hádané písmeno"""
    seznam = list(nahodne_slovo)
    seznam_indexu = []
    for cislo, character in enumerate(seznam):
        if seznam[cislo] == pismeno:
            seznam_indexu.append(cislo)
    for x in seznam_indexu:
        zacatek = pole[:x]
        #prostredek = pismeno
        konec = pole[x+1:]
        pole = zacatek + pismeno + konec
    return pole

def hadej_pismeno():
    pismeno = input("Hádej písmeno: ").lower()
    while True:
        if pismeno in "abcdefghijklmnopqrstuvwxyzáéíóúůýžšččřďťňě" and len(pismeno) == 1:
            return pismeno
        else:
            pismeno = input("Hádej jedno písmeno, které není speciální znak: ").lower()

def hra():
    slovo = nahodne_slovo()
    pole = "_" * len(slovo)
    neuspesne_pokusy = 0
    print(pole)
    while "_" in pole:
        pismeno = hadej_pismeno()
        pole = zamen(slovo, pole, pismeno)
        if pismeno not in pole:
            neuspesne_pokusy += 1
        print(pole)
        print(f'Neúspěšné pokusy: {neuspesne_pokusy}')
        print(obrazek(neuspesne_pokusy))
    znova = input("Gratuluju k výhře, chceš si zahrát znova? ano/ne: ")
    while znova not in ("ano", "ne"):
        znova = input('Zadej jen slovo "ano" nebo "ne": ')
    return znova

vysledek = hra()

while True:
    if vysledek == "ano":
        vysledek = hra()
    elif vysledek == "ne":
        print("Škoda.")
        break