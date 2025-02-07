import operator
MAX_LEVEL = 200

def leggi_file(nome_file):
    pazienti = dict()
    file = open(nome_file, 'r')
    
    for line in file:
        campi = line.strip().split(' ')
        codice = campi[0]
        ora = campi[1]
        valore = int(campi[2])
        
        if valore >= MAX_LEVEL:
            if codice not in pazienti:
                pazienti[codice] = {
                    'codice': codice,
                    'n_sup': 1,
                    'sup': [ora + ' ' + str(valore)]
                }
            else:
                pazienti[codice]['n_sup'] += 1
                pazienti[codice]['sup'].append(ora + ' ' + str(valore))
        
    file.close()
    return pazienti

def stampa_superamenti(pazienti):
    # ordina in modo decrescente per numero di superamenti
    lista = sorted(pazienti.values(), key=operator.itemgetter('n_sup'), reverse = True)
    for paziente in lista:
        codice = paziente['codice']
        for value in paziente['sup']:
            print(codice, value)
        print()

def main():
    print()
    pazienti = leggi_file('glucometers.txt')
    stampa_superamenti(pazienti)
    
main()