import math

nomi_file = ['matrices.txt', 'matrices_error.txt', 'matrices_large.txt']

def leggi_matrici(nome_file):
    sequenza = list()
    
    file = open(nome_file, 'r')
    for line in file:
        matrix = dict()
        values = line.strip().split(' ')
        matrix['r'] = int(values[0])
        matrix['c'] = int(values[1])
        matrix['mat'] = list()
        for i in range(matrix['r']):
            row = list()
            for j in range(matrix['c']):
                row.append(int(values[2 + i*matrix['c'] + j]))
            matrix['mat'].append(row)
        sequenza.append(matrix)
        
    return sequenza

def prodotto_matrice(matA, matB):
    product = dict()
    product['mat'] = list()
    product['r'] = matA['r']
    product['c'] = matB['c']
    common_dim = matA['c']
    A = matA['mat']
    B = matB['mat']
    
    print(f"({matA['r']}, {matA['c']}) x ({matB['r']}, {matB['c']}) = ({matA['r']}, {matB['c']})")
    for i in range(product['r']):
        row = list()
        for j in range(product['c']):
            value = 0
            for k in range(common_dim):
                value = value + A[i][k] * B[k][j]
            row.append(value)
        product['mat'].append(row)
    
    return product

def controllo(matA, matB):
    if matA['c'] == matB['r']:
        return True
    
    return False

def controlla_matrici(sequenza):
    for i in range(len(sequenza)-1):
        if controllo(sequenza[i], sequenza[i+1]) is False:
            return False
        
    return True

def stampa_dimensioni(sequenza):
    print("| ", end = "")
    for matrice in sequenza:
        print(f"{matrice['r']} x {matrice['c']} | ", end = "")
    print()

def moltiplica_matrici(sequenza):
    while len(sequenza) > 1:
        stampa_dimensioni(sequenza)
        min_index = costo_minimo(sequenza)
        A = sequenza[min_index]
        B = sequenza[min_index+1]
        sequenza[min_index] = prodotto_matrice(A, B)
        sequenza.pop(min_index+1)
        print()
        
def costo_minimo(sequenza):
    min_index = -1
    min = math.inf
        
    for i in range(len(sequenza)-1):
            A = sequenza[i]
            B = sequenza[i+1]
            costo = A['r'] * A['c'] * B['c']
            if costo < min:
                min_index = i
                min = costo
                
    return min_index

def stampa_matrice(matrice):
    r = matrice['r']
    c = matrice['c']
    mat = matrice['mat']
    
    for i in range(r):
        print("\t", end="")
        for j in range(c):
            print(mat[i][j], end = "\t")
        print()

def main():
    for nome_file in nomi_file:
        print(f"--- File: {nome_file} ---")
        # ottieni dati
        sequenza = leggi_matrici(nome_file)
        
        # se la sequenza non ha dimensioni valide, la sequenza non è moltiplicabile
        if controlla_matrici(sequenza) is False:
            print('Le matrici non possono essere moltiplicate.')
            print()
            continue
        
        # moltiplica le matrici
        moltiplica_matrici(sequenza)
        
        # stampa la matrice ottenuta
        stampa_matrice(sequenza[0])
        print()
    
main()