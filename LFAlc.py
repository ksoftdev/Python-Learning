import os
        
def mostrarAlcanzables(ALC):
    print( '{' + ''.join(ALC) + '}')

def joinC(l):
    nl = ''
    for i in l:
        if i != 'lambda':
            nl += i
    return nl

def getNALC(ALC, G, V, C):
    N = []
    print('Testing: ', C)
    for i in C:
        if ( i in V and not i in ALC and not i in N):
            N.append(i)
            print('N: ', N)
            del G[i]
    return N

def calcularAlcanzables(G, V):
    GiC = G.copy()
    ALC = ['S']
    al = joinC(GiC['S'])
    del GiC['S']
    C = GiC
    NALC = getNALC(ALC, GiC, V, al)
    ALC += NALC
    
    i = 1
    while ( NALC ):
         for x in range(i, len(ALC)):
            NALC = getNALC(ALC, GiC, V, joinC(G[ALC[i]]))
            ALC += NALC
            i += 1
    return GiC

if __name__ == '__main__':
    G = {}
    V = []

    n_prod = int(input())
    for i in range(n_prod):
        line =  input().split('->')
        k = line[0].rstrip()
        v = line[1].split('|')
        for i in range(len(v)):
            v[i] = v[i].rstrip().lstrip()
        G.update({k : v})
        V.append(k)
    
    ALC = calcularAlcanzables(G, V)
    mostrarAlcanzables(ALC)
