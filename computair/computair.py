def leggi_voli(nome_file):
    voli = {}
    
    file = open(nome_file, 'r')
    for line in file:
        valori = line.strip().split(';')
        
        voli[valori[0]] = {
            "destinazione": valori[1],
            "passeggeri": int(valori[2])
        }
    
    file.close()
    return voli

def leggi_meteo(nome_file):
    meteo = {}
    
    file = open(nome_file, 'r')
    for line in file:
        valori = line.strip().split(';')
        
        meteo[valori[0]] = valori[1]
        
    file.close()
    return meteo

def media_passeggeri(voli):
    media = 0
    n = 0
    for codice in voli:
        media = media + voli[codice]["passeggeri"]
        n = n + 1
    media = '%.1f' % (media/n)
    print(f"Numero medio di passeggeri: {media}")
    
    print()

def meteo_RS(voli, meteo):
    condizioni = ["Rainy", "Stormy"]
    print("Codice dei voli verso città con condizione meteorologica Rainy o Stormy:")
    for codice in voli:
        destinazione = voli[codice]["destinazione"]
        if meteo[destinazione] in condizioni:
            print(f"* {codice} verso {destinazione}: {meteo[destinazione]}")
    
    print()
    
def info_citta(voli, meteo):    
    citta = {}
    for codice in voli:
        destinazione = voli[codice]["destinazione"]
        passeggeri = voli[codice]["passeggeri"]
        if destinazione not in citta:
            citta[destinazione] = {
                "meteo": meteo[destinazione],
                "passeggeri": 0
            }
        
        citta[destinazione]["passeggeri"] = citta[destinazione]["passeggeri"] + passeggeri
    
    print("Condizione meteorologica delle città che sono destinazione di almeno un volo:")
    for destinazione in citta:
        print(f"* {destinazione}: {citta[destinazione]['meteo']}.",
              f"{citta[destinazione]['passeggeri']} passeggeri in arrivo.")
    
    print()

def main():
    voli = leggi_voli('flights.txt')
    meteo = leggi_meteo('weather.txt')

    print()
    media_passeggeri(voli)
    meteo_RS(voli, meteo)
    info_citta(voli, meteo)
    
main()
    