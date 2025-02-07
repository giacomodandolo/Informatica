def leggi_presenze(nome_file):
    presenze = dict()
    
    file = open(nome_file, 'r')
    for line in file:
        values = line.strip().split(',')
        presenze[values[0]] = {
            'numTel': values[1],
            'dayStart': int(values[2]),
            'dayEnd': int(values[3])
        }
    file.close()
    
    return presenze

def valuta_sospetti(nome_file, presenze):
    file = open(nome_file, 'r')
    for sospetto in file:
        print()
        sospetto = sospetto.strip() # evitare caratteri whitespaces
        print(f"** Contatti del cliente: {sospetto} **")
        # se il sospetto non è tra le presenze
        if sospetto not in presenze.keys():
            print(f"Cliente {sospetto} non presente in archivio.")
            continue
        
        sospetto_dict = presenze[sospetto]
        trovato = False
        for nome in presenze:
            corrente = presenze[nome]
            # se si sta considerando il sospetto stesso oppure i tempi non si intersecano
            if  (nome == sospetto or 
                (corrente['dayStart'] > sospetto_dict['dayEnd'] 
                 or corrente['dayEnd'] < sospetto_dict['dayStart'])):
                continue
            trovato = True
            print(f"Contatto con {nome}, telefono {corrente['numTel']}")
        
        # se non è stata trovata alcuna intersezione
        if trovato == False:
            print(f"Il cliente {sospetto} non ha avuto contatti")
    
    file.close()

def main():
    presenze = leggi_presenze('presenze.txt')
    
    valuta_sospetti('sospetti.txt', presenze)
    print()
    
main()