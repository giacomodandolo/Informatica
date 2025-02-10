import math

# leggi il file listino
def leggi_listino(nome_file):
    listino = {}
    
    file = open(nome_file, 'r')
    for line in file:
        valori = line.strip().split(' ')
        if len(valori) > 3:
            for i in range(2, len(valori)-1):
                valori[1] = valori[1] + ' ' + valori[i]
                valori.pop(i)
        # lettera associata a {'città': città, 'prezzo': prezzo}
        listino[valori[0]] = {
            'nome': valori[1],
            'prezzo': int(valori[2])
        }
    
    file.close()
    return listino

# leggi il file distanze
def leggi_distanze(nome_file):
    distanze = []
    
    file = open(nome_file, 'r')
    for line in file:
        valori = line.strip().split(':')
        tratte = valori[0].split('-')
        # {'partenza': lettera di partenza, 'destinazione': lettera di destinazione, 'km': km della tratta}
        distanza = {
            'partenza': tratte[0], 
            'destinazione': tratte[1],
            'km': int(valori[1])
        }
        
        distanze.append(distanza)

    file.close()
    return distanze

# ottieni le città direttamente connesse alla prima città del file
def ottieni_citta_connesse(listino, distanze):
    connesse = []
    
    for tratta in distanze:
        if tratta['partenza'] == 'a':
            connesse.append(listino[tratta['destinazione']]['nome'])
        
    return connesse

# stampa le città connesse
def stampa_connesse(connesse):
    print(f"Città direttamente connesse a Los Angeles:")
    for connessa in connesse:
        print(connessa)

# ottieni il pezzo di tratta per arrivare alla città definita da lettera
def trova_tratta(distanze, lettera):
    for i, tratta in enumerate(distanze):
        if tratta['destinazione'] == lettera:
            return i
    
    return -1 # se non trova

# ottieni l'effettiva distanza verso una determinata lettera
def ottieni_distanza(distanze, lettera):
    last = trova_tratta(distanze, lettera)
    km = 0

    while distanze[last]['partenza'] != 'a':
        attuale = distanze[last]['partenza']
        km = km + distanze[last]['km']
        last = trova_tratta(distanze, attuale)
    
    km = km + distanze[last]['km']
    return km

# ottieni l'offerta massima tra quelle del listino
# soglia utilizzato per capire se deve esserci un limite
# massimo di distanza, se -1 allora non c'è un limite
def ottieni_offerta_max(listino, distanze, soglia):
    max = 0
    max_citta = ""
    
    for codice in listino:
        if soglia != -1:
            if ottieni_distanza(distanze, codice) <= soglia and max < listino[codice]['prezzo']:
                max = listino[codice]['prezzo']
                max_citta = codice
                continue
        elif max < listino[codice]['prezzo']:
            max = listino[codice]['prezzo']
            max_citta = codice
    
    return max_citta

# ottieni il rapporto offerta/distanza peggiore
def ottieni_peggior_rapporto(listino, distanze):
    min = math.inf
    min_citta = ""
    
    for codice in listino:
        if codice == 'a':
            continue
        
        distanza = ottieni_distanza(distanze, codice)
        offerta = listino[codice]['prezzo']
        
        corrente = offerta/distanza
        if min > corrente:
            min = corrente
            min_citta = listino[codice]['nome']
    
    return min_citta

def main():
    listino = leggi_listino('listino.txt')
    distanze = leggi_distanze('distanze.txt')
    
    print()
    connesse = ottieni_citta_connesse(listino, distanze)
    stampa_connesse(connesse)
    
    print()
    citta_offerta_max = ottieni_offerta_max(listino, distanze, -1)
    distanza_max = ottieni_distanza(distanze, citta_offerta_max)
    print(f"Offerta migliore: {listino[citta_offerta_max]['nome']} - {distanza_max} km")
    
    citta_peggior_rapporto = ottieni_peggior_rapporto(listino, distanze)
    print(f"Città con il peggior rapporto offerta/km:", citta_peggior_rapporto)
    
    citta_offerta_soglia = ottieni_offerta_max(listino, distanze, 4000)
    distanza_soglia = ottieni_distanza(distanze, citta_offerta_soglia)
    print(f"Offerta migliore sotto i 4000 km: {listino[citta_offerta_soglia]['nome']} - {distanza_soglia} km")
    print()
    return

main()