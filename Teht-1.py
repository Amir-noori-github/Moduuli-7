# Python Moduuli - 7 Tehtävä-1

def hae_vuodenaika(kk_numero):

    vuodenajat = {
        "talvi": [12, 1, 2],
        "kevät": [3, 4, 5],
        "kesä": [6, 7, 8],
        "syksy": [9, 10, 11]
    }

    for vuodenaika, kuukaudet in vuodenajat.items():
        if kk_numero in kuukaudet:
            return vuodenaika

    return "Virheellinen kuukauden numero"

try:
    kk_numero = int(input("Anna kuukauden numero (1-12): "))
    if 1 <= kk_numero <= 12:
        vuodenaika = hae_vuodenaika(kk_numero)
        print(f"Kuukautta {kk_numero} vastaa vuodenaika: {vuodenaika}.")
    else:
        print("Virhe: Anna luku välillä 1-12.")
except ValueError:
    print("Virhe: Anna kelvollinen kokonaisluku.")
