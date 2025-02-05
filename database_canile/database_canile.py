def leggi_file(nome_file):
    file = open(nome_file, 'r')
    
    # Creo la struttura dati
    #   lista per tutti i cani
    #   per ogni cane, un dizionario con le sue informazioni
    cani_list = list()
    intestazioni = file.readline().split(',')
    for line in file:
        cane = dict()
        line_split = line.split(',')
        for i, caratteristica in enumerate(intestazioni):
            cane[caratteristica] = line_split[i].strip()
        cani_list.append(cane)
    
    file.close()
    
    return [intestazioni, cani_list]

def main():
    [intestazioni, cani] = leggi_file('dogs.csv')
    razze = list()
    livelli = ("Beginner", "Intermediate", "Advanced", "Expert")
    
    # ottengo la lista delle razze da valutare
    for cane in cani:
        if cane[intestazioni[2]] not in razze:
            razze.append(cane[intestazioni[2]])
    
    # valuto ogni razza
    for razza in razze:
        print(f"\nRazza: {razza}")
        # per ogni razza, valuto il livello
        for livello in livelli:
            media = 0
            n = 0
            for cane in cani:
                if cane[intestazioni[2]] == razza and cane[intestazioni[3]] == livello:
                    media = media + float(cane[intestazioni[4]])
                    n = n + 1
            # se c'è almeno un cane per quel livello, allora stampo
            if n > 0:
                media = "%.2f" % (media/n)
                print(f"\tLivello {livello}: \t\t{media}")

    print("\n")
    
main()