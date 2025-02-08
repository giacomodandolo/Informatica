def leggi_personaggi(nome_file):
    file = open(nome_file, 'r')

    proprieta = file.readline().strip().split(';') # ["Colore Capelli", "Occhi", "Occhiali"]

    # lista di personaggi (dizionari)
    personaggi = []

    for line in file:
        valori = line.strip().split(';')
        personaggio = {}
        for i in range(len(proprieta)): # 0 -> numero di proprietà - 1
            personaggio[proprieta[i]] = valori[i]
        personaggi.append(personaggio)
    
    file.close()
    return personaggi

def gioca_partita(nome_file, personaggi):
    # copio la lista di personaggi
    personaggi_in_gioco = list(personaggi)  

    file = open(nome_file, 'r')
    mosse = 0
    for line in file:
        [proprieta, valore] = line.strip().split('=')
        mosse += 1
        print(f'\nMossa {mosse} - Domanda: {proprieta} = {valore} ?')
        
        # definisco la lista di personaggi rimanenti
        tmp = list()
        for p in personaggi_in_gioco:
            if p[proprieta] == valore:
                tmp.append(p)
        personaggi_in_gioco = list(tmp)
        
        # stampo la lista di personaggi rimanenti
        print('Personaggi selezionati:')
        for personaggio in personaggi_in_gioco:
            for proprieta in personaggio:
                print(f'{proprieta}={personaggio[proprieta]}', end='  ')
            print()

    # decido se con questa partita si vince o si perde
    if len(personaggi_in_gioco) == 1:
        print("Hai vinto!")
    else:
        print("Hai perso...")
    
    file.close()

def main():
    personaggi = leggi_personaggi('personaggi.txt')
    # print(personaggi)
    domande = ['domande1.txt', 'domande2.txt']

    for file_domanda in domande:
        print(f"\n\n--- {file_domanda} ---")
        gioca_partita(file_domanda, personaggi)
    
main()
