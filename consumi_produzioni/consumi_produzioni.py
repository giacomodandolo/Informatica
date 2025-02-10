import operator

def leggi_file(nome_file):
    lista = list()
    file = open(nome_file, 'r')
    
    chiavi = file.readline().strip().split(';')
    
    for line in file:
        valori = line.strip().split(';')
        diz = dict()
        for i in range(len(chiavi)):
            diz[chiavi[i]] = valori[i]
        lista.append(diz)
    
    file.close()
    return lista

def ordina_key(abitazioni, key):
    lista = sorted(abitazioni.values(), key=operator.itemgetter(key), reverse=True)
    print(key, "maggiore:", end=" ")
    for i in range(3):
        print(lista[i]['ID'], end=" ")
    print()

def energia_abitazioni(consumi, impianti, meteo):
    energia_ab = {}
    prodotta = consumata = autocons = immessa = 0.0
    
    for impianto in impianti:
        ID = impianto['ID_Abitazione']
        efficienza = float(impianto['Eta'])
        dimensione = float(impianto['Dimensione_impianto'])
        energia_ab[ID] = {
            'ID': ID,
            'en_prodotta': 0.0,
            'en_consumata': 0.0,
            'en_immessa': 0.0,
            'en_autoconsumata': 0.0,
            'perc_autocons': 0.0,
            'perc_autosuff': 0.0
        }
        attuale = energia_ab[ID]
        for consumo in consumi:
            if consumo['ID_Abitazione'] != ID:
                continue
            
            data = consumo['Data']
            ora = consumo['Ora']
            consumo_en = float(consumo['Consumo_energetico'])
            radiazione_solare = 0
            for momento in meteo:
                if data == momento['DATA'] and ora == momento['ORA']:
                    radiazione_solare = float(momento['GHI'])
                    break
            
            attuale['en_prodotta'] += efficienza*dimensione*radiazione_solare
            attuale['en_consumata'] += consumo_en
            tmp = efficienza*dimensione*radiazione_solare - consumo_en
            if tmp > 0:
                attuale['en_immessa'] += tmp
        attuale['en_autocons'] = attuale['en_prodotta'] - attuale['en_immessa']
        attuale['perc_autocons'] = (attuale['en_autocons']/attuale['en_prodotta'])*100
        attuale['perc_autosuff'] = (attuale['en_autocons']/attuale['en_consumata'])*100
        
        prodotta += attuale['en_prodotta']
        consumata += attuale['en_consumata']
        autocons += attuale['en_autocons']
        immessa += attuale['en_immessa']
        
    print("--- Report Aggregato ---\n",
          f" Energia Prodotta: {'%.2f' % prodotta} kWh\n",
          f" Energia Consumata: {'%.2f' % consumata} kWh\n",
          f" Energia Autoconsumata: {'%.2f' % autocons} kWh\n",
          f" Energia Immessa: {'%.2f' % immessa} kWh\n",
          f" Percentuale Autoconsumo: {'%.2f' % ((autocons/prodotta)*100)}%\n",
          f" Percentuale Autosufficienza: {'%.2f' % ((autocons/consumata)*100)}%\n")
    
    ordina_key(energia_ab, 'perc_autocons')
    ordina_key(energia_ab, 'perc_autosuff')
    

def main():
    consumi = leggi_file('consumi.txt')
    impianti = leggi_file('impianti.txt')
    meteo = leggi_file('meteo.txt')
    
    energia_abitazioni(consumi, impianti, meteo)

main()