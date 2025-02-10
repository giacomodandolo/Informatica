import operator

def leggi_comuni(nome_file):
    comuni = []
    file = open(nome_file, 'r')
    file.readline()
    
    for line in file:
        valori = line.strip().split(';')
        comune = {
            'nome_comune': valori[6],
            'nome_regione': valori[10]
        }
        
        comuni.append(comune)

    file.close()
    return comuni

def leggi_regioni(nome_file):
    regioni = []
    file = open(nome_file, 'r')
    
    for line in file:
        regione = line.strip()
        regioni.append(regione)
    
    file.close()
    return regioni

def trova_numero_comuni(comuni, regione):
    n = 0
    
    for comune in comuni:
        if comune['nome_regione'] == regione:
            n = n + 1
    
    return n

def comune_caratteri_min(comuni, regione):
    min = ""
    comuni_ordinato = sorted(comuni, key=operator.itemgetter('nome_comune'))
    
    for comune in comuni_ordinato:
        if comune['nome_regione'] == regione:
            if len(min) == 0 or len(min) > len(comune['nome_comune']):
                min = comune['nome_comune']
    
    return min

def comune_caratteri_max(comuni, regione):
    max = ""
    comuni_ordinato = sorted(comuni, key=operator.itemgetter('nome_comune'))
    
    for comune in comuni_ordinato:
        if comune['nome_regione'] == regione:
            if len(max) == 0 or len(max) < len(comune['nome_comune']):
                max = comune['nome_comune']
    
    return max

def main():
    comuni = leggi_comuni('elenco-comuni-italiani.csv')
    regioni = leggi_regioni('regioni.txt')
    
    for regione in regioni:
        print()
        print(regione)
        print("* Numero comuni:", trova_numero_comuni(comuni, regione))
        min = comune_caratteri_min(comuni, regione)
        max = comune_caratteri_max(comuni, regione)
        print("* Comune con il nome di lunghezza minima:", min)
        print("* Comune con il nome di lunghezza massima:", max)

    print()
    return
    
main()