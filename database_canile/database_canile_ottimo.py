def leggi_file(nome_file):
    cani = {}
    
    file = open(nome_file, 'r')
    file.readline()
    for line in file:
        campi = line.strip().split(',')
        
        razza = campi[2]
        livello = campi[3]
        punteggio = float(campi[4])
        
        if razza not in cani:
            cani[razza] = {
                'Beginner': [0.0, 0],
                'Intermediate': [0.0, 0],
                'Advanced': [0.0, 0],
                'Expert': [0.0, 0]
            }

        cani[razza][livello][0] = cani[razza][livello][0] + punteggio
        cani[razza][livello][1] = cani[razza][livello][1] + 1
    
    file.close()
    return cani

def main():
    cani = leggi_file('dogs.csv')
    
    for razza in cani:
        print(f"\nRazza: {razza}")
        for livello in cani[razza]:
            valori = cani[razza][livello]
            if valori[1] != 0:
                media = "%.2f" % (valori[0]/valori[1])
                print(f"\tLivello {livello}: \t\t{media}")
                
main()