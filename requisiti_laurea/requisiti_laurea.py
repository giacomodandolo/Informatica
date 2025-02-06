import operator


def leggi_esami(nome_file):
    esami = []
    with open(nome_file, "r") as f:
        for riga in f:
            campi = riga.strip().split(",")

            campi[1] = "/".join(campi[1].split("/")[::-1])  # divide la data, inverte i valori 
                                                            # [GG,MM,AAAA] -> [AAAA,MM,GG]
                                                            # reinserisce i caratteri '\'

            esami.append(campi)
    return esami


def leggi_cfu(nome_file):
    cfu = {}
    with open(nome_file, "r") as f:
        for riga in f:
            campi = riga.strip().split(",")
            # codice -> {'crediti': crediti, 'obbligatorio': T/F}
            cfu[campi[0]] = {
                "crediti": int(campi[1]),
                "obbligatorio": bool(int(campi[2])),
            }
    return cfu


def ottieni_voti(esami):
    studenti = dict()
    
    for esame in esami:
        matricola = esame[0]
        codice = esame[2]
        voto = esame[3]

        if voto != "A" and voto != "R":
            if matricola not in studenti:
                studenti[matricola] = dict()

            studenti[matricola][codice] = voto
    
    return studenti


def calcola_media(studenti, matricola, cfu):
    tot_crediti = 0
    tot_crediti_obbligatori = 0
    media = 0.0

    print(f"media di {matricola}")
    for codice in studenti[matricola]:
        crediti = cfu[codice]["crediti"]
        obbligatorio = cfu[codice]["obbligatorio"]
        voto = studenti[matricola][codice]
        if voto == "30L":
            voto = 33
        else:
            voto = int(voto)
            
        tot_crediti = tot_crediti + crediti
        if obbligatorio:
            tot_crediti_obbligatori = tot_crediti_obbligatori + crediti
        media = media + voto * crediti
        
    media = media / tot_crediti
    print(f"CFU totali {tot_crediti}, CFU obbligatori {tot_crediti_obbligatori}, media {media}")
    if tot_crediti >= 30 and tot_crediti_obbligatori >= 10:
        print("Ammissibile")
    else:
        print("Non ammissibile")


def main():
    esami = leggi_esami("esami.log")

    cfu = leggi_cfu("cfu.dati")

    ## ordina la lista degli esami per data crescente
    esami.sort(key=operator.itemgetter(1))

    studenti = ottieni_voti(esami)
    
    for matricola in studenti:
        calcola_media(studenti, matricola, cfu)


main()
