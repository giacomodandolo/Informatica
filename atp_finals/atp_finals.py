from random import randint

def ottieni_giocatori():
    file = open('qualificati.txt', 'r')
    giocatori = []
    
    for line in file:
        nome = (line.split(","))[1]
        giocatori.append(nome)
    
    file.close()
    return giocatori

def ottieni_gruppi(giocatori):
    gruppo_A = [0]
    gruppo_B = [1]
    
    for i in range(2, len(giocatori), 2):
        k = randint(0,1)
        gruppo_A.append(i + k)
        gruppo_B.append(i + 1 - k)
    
    return [gruppo_A, gruppo_B]

def gruppo_in_file(nome_file, gruppo, giocatori):
    file = open(nome_file, 'w')
    
    for index in gruppo:
        file.write(f'{index+1} - {giocatori[index]}')
    
    file.close()

def entry(file, girone, gruppo, giocatori, days):
    file.write(f'GIRONE {girone}\n')
    combinazioni = [] # tenere traccia delle combinazioni già avvenute
    
    for day in range(days):
        file.write(f'Giornata {day+1}:\n')
        usato = set() # serve per non avere duplicati nella stessa giornata
        while len(usato) is not len(gruppo): # vado avanti fino a quando non ho usato tutti i giocatori
            i = j = 0
            while(i == j or i in usato or j in usato):
                i = randint(0, len(gruppo)-1)
                j = randint(0, len(gruppo)-1)
            
            if ((i,j) in combinazioni):
                continue
            
            combinazioni.append((i,j)) # (1,2) <-X-> (2,1)
            combinazioni.append((j,i))
            usato.add(i)
            usato.add(j)
            
            i_1 = gruppo[i]
            i_2 = gruppo[j]
            
            file.write(f'{giocatori[i_1]} vs {giocatori[i_2]}')
    
def crea_calendario(giocatori, gruppo_A, gruppo_B):
    file = open('calendario.txt', 'w')
    
    # print(gruppo_A)
    entry(file, 'VERDE', gruppo_A, giocatori, 3)
    file.write('\n')
    # print(gruppo_B)
    entry(file, 'ROSSO', gruppo_B, giocatori, 3)
    
    file.close()    

def main():
    giocatori = ottieni_giocatori()
    
    [gruppo_A, gruppo_B] = ottieni_gruppi(giocatori)
    
    gruppo_in_file('verde.txt', gruppo_A, giocatori)
    gruppo_in_file('rosso.txt', gruppo_B, giocatori)
    
    crea_calendario(giocatori, gruppo_A, gruppo_B)

main()
        