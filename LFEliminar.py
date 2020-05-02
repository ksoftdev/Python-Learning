import os

# 
def mostrarGI(G):
    for k, v in G.items():
        print(k + ' -> ' + ' | '.join(v) )

# 
def mostrarG(G):
    for k, v in G.items():
        print(k, ': ', v)

# 
def joinC(l):
    nl = ''
    for i in l:
        if i != 'lambda':
            nl += i
    return nl

# 
def getNALC(ALC, G, V, C):
    N = []
    print('Testing: ', C)
    for i in C:
        if ( i in V and not i in ALC and not i in N):
            N.append(i)
            print('N: ', N)
            del G[i]
    return N

# 
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
    return [GiC, ALC]

# 
def calcularTerminables(G, V):
    NTERM = G.copy()
    TERM = []
    C = TERM

    i = 1
    while ( True ):
        if ( i == 1 ):
            for k, v in NTERM.items():
                for val in v:
                    if not any( item in V for item in list(val) ) or val == 'lambda':
                        TERM.append(k)
            for d in TERM:
                del NTERM[d]
        else:
            while ( C ):
                print('\nTERM')
                print(TERM)
                print('\nNTERM')
                mostrarG(NTERM)
                
                C = []
                
                for k, v in NTERM.items():
                    for prod in v:
                        isterm = True
                        for item in prod:
                            if ( item in V ):
                                isterm = isterm and ( item in TERM )
                        if ( isterm ):
                            C.append(k)
                            break
                TERM += C
                for d in C:
                    del NTERM[d]
            break
        i += 1
    return [TERM, list(NTERM.keys())]

#
def calcularG1(T, G):
    G1 = G.copy()
    NTERMS = T[1][0]
    del G1[NTERMS]
    
    for k , v in G1.items():
        for item in v:
            if NTERMS in item:
                v.remove(item)
                
    print('Gramatica G1 equivalente')
    mostrarG(G1)

    return G1

# 
def calcularG2(T, G1):
    G2 = G1.copy()
    for k in T[0].keys():
        del G2[k]
    
    print('Gramatica G2 sin variables inutiles')
    mostrarG(G2)
    return G2

#  
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
        V.append(k)
        G.update({k : v})
    
    print('G')
    mostrarG(G)
    G1 = calcularG1(calcularTerminables(G, V), G)
    G2 = calcularG2(calcularAlcanzables(G1, V), G1)
    mostrarGI(G2)
    
