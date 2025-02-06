chiavi = []

def leggi_dati(nome_file):
    global chiavi
    file = open(nome_file, 'r')
    collezione = list()
    # ottieni chiavi
    chiavi = file.readline().strip().split(',')
    # per ogni riga ottieni le informazioni
    for line in file:
        musica = dict()
        i = 0
        valori = line.strip().split(',')
        for chiave in chiavi:
            musica[chiave] = valori[i]
            i = i + 1
        collezione.append(musica)
    file.close()

    return collezione

def gestisci_interrogazioni(nome_file, collezione):
    file = open(nome_file, 'r')
    for line in file:
        interrogazione = line.strip().split(':')
        tipo = interrogazione[0]
        info = interrogazione[1]
        
        if tipo == 'c': # compositore
            stampa_compositore(info, collezione)
        elif tipo == 's': # formazione musicale
            stampa_formazione_musicale(info, collezione)
        
        print()
    
    file.close()

def stampa_compositore(compositore, collezione):
    brani_unici = dict() # dizionario dei brani unici
    presente = False
    
    # ottengo tutti i brani unici del compositore
    for brano in collezione:
        comp = brano[chiavi[1]] # compositore
        composizione = brano[chiavi[2]] # composizione
        nome_catalogo = brano[chiavi[5]] # nome da catalogo
        if comp == compositore and nome_catalogo not in brani_unici:
            brani_unici[nome_catalogo] = composizione
            presente = True
    
    if presente is False:
        print(f"{compositore}: compositore non presente nel catalogo.")
        return
    
    print(f"Opere di {compositore}")
    # per ogni brano unico, ottengo e stampo le informazioni volute
    for nc in brani_unici:
        durata = 0
        n = 0
        for brano in collezione: # per ogni brano di collezione
            nome_catalogo = brano[chiavi[5]]
            add_value = float(brano[chiavi[6]])
            if nc == nome_catalogo: # se il nome catalogo è lo stesso
                durata = durata + add_value
                n = n + 1
        
        media = "%.2f" % (durata/n)
        durata = "%.2f" % durata
        print(f"- {nc}: {brani_unici[nc]}, {durata} secondi")
        print(f"\t{n} movimenti, in media {media} secondi")

def stampa_formazione_musicale(formazione_musicale, collezione):
    presente = False
    stampati = set()
    
    # per ogni brano, se la formazione combacia stampa le informazioni
    for brano in collezione:
        compositore = brano[chiavi[1]]
        formazione = brano[chiavi[4]]
        nome_catalogo = brano[chiavi[5]]
        if formazione == formazione_musicale and nome_catalogo not in stampati:
            if presente is False:
                print(f"Opere con formazione musicale: {formazione_musicale}")
                presente = True
            print(f"- {compositore}, opera {nome_catalogo}")
            stampati.add(nome_catalogo)

    if presente is False:
        print(f"{formazione_musicale}: formazione musicale non presente nel catalogo.")
    
def main():
    collezione = leggi_dati('musicnet.csv')
    gestisci_interrogazioni('richieste.txt', collezione)

main()
