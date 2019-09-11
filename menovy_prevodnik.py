import requests
'''
#kurzovní lístek pro daný den:
datum = str(input("Zadej datum ve formátu DD.MM.RRRR, pro který bys chtěl vypsat kurzovní lístek: "))
url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=" + datum
print(url)
response = requests.get(url)
print(response.text)
'''
mena = input("Zadej kód měny, pro kterou chceš kurz: ")
mena = mena.upper()
mnozstvi = int(input("Zadej, kolik máš korun, a já ti řeknu, kolik si můžeš koupit dané měny: "))

listek = requests.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt")
listek = str(listek.text)
listek = listek.replace(",", ".")

listek = listek.split('\n')
del listek[0:2]
del listek[-1]

podseznamy = []

for element in listek: # rozdělení seznamu na podseznamy
	cast = element.split('|')
	podseznamy.append(cast)

for i in range(len(podseznamy)): # spočítá množství peněz v dané měně
	if mena == podseznamy[i][3]:
		vypocet = round(mnozstvi*int(podseznamy[i][2])/float(podseznamy[i][4]),2)
		print(f'Za {mnozstvi} korun dostaneš {vypocet} {mena}.')

#print(podseznamy)


