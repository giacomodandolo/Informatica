def main():
    with open ('brani.txt', 'r', encoding='utf-8') as file:
    #brani sarà una lista di liste, ogni lista al suo interno contiene le informazioni su un brano
        brani = []
        for line in file:
    
        #divido la riga tra prima e dopo i ":"
            line = line.strip().split(":")

            #ciò che c'è prima dei ":" è il nome del brano
            nomebrano = line[0]

            #ciò che c'è dopo è l'insieme delle note, che divido in base agli spazi
            note = line[1].split(" ")
        
            #infobrano sarà una lista che in prima posizione ha il nome del brano e poi
            #tutte le note che lo compongono
            infobrano = []
            infobrano.append(nomebrano)
            for i in range(len(note)):
                cleaned_note=note[i].strip()
                if cleaned_note:
                    infobrano.append(int(note[i]))

            #aggiungo le informazioni su questo brano nella lista "brani"
            brani.append(infobrano)

        #per ogni brano
        for i in range(len(brani)):

            #effettuo un confronto con quelli precedenti
            for j in range(i):
                ControllaPlagio(brani[i], brani[j])
        

    return 0


def ControllaPlagio(brano1, brano2):
    #STEP 1 : Verifico che i brani siano uguali

    uguali = True
    for i in range(1, len(brano1)):
        if brano1[i] != brano2[i]:
            uguali = False
            break

    if uguali:
        print(f"PLAGIO: \t{brano1[0]} | {brano2[0]}")
        return
    

    #STEP 2 : Se non sono uguali, verifico la copiatura
    # +
    #STEP 3 : Se non sono uguali e non è una copiatura verifico se sia un sospetto
    for i in range(1, len(brano1)-3):
        for j in range(1, len(brano2)-3):
            distanza = brano1[i] - brano2[j]
            # controllo copiatura
            if distanza == 0:
                uguali = True
                for k in range(4):
                    if (brano1[i+k] != brano2[j+k]):
                        uguali = False
                        break

                if uguali:
                    print(f"COPIATURA: \t{brano1[0]} | {brano2[0]}")
                    return
            # controllo sospetto
            else:
                plagio = True
                for k in range(4):
                    if (brano1[i+k] - brano2[j+k] != distanza):
                        plagio = False
                        break

                if plagio:
                    print(f"SOSPETTO: \t{brano1[0]} | {brano2[0]}")
                    return
                


main()