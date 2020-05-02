import os

def mostrarG(G):
    for k, v in G.items():
        print(k, ': ', v)
        
def mostrarTerminables(TERM):
    print( '{' + ''.join(TERM) + '}')

def calcularTerminables(G, V):
    NTERM = G.copy()
    TERM = []
    C = TERM

    i = 1
    while ( True ):
        if ( i == 1 ):
            for k, v in NTERM.copy().items():
            	for val in v:
                	if not any( item in V for item in list(val) ) or val == 'lambda':
                	    TERM.append(k)
                	    del NTERM[k]
        else:
            while ( C ):
                print('\nTERM')
                print(TERM)
                print('\nNTERM')
                mostrarG(NTERM)
                
                C = []
                
                for k, v in NTERM.copy().items():
                    for prod in v:
                        isterm = True
                        for item in prod:
                            if ( item in V ):
                                isterm = isterm and ( item in TERM )
                        if ( isterm ):
                            C.append(k)
                            del NTERM[k]
                            break
                TERM += C
            break
        i += 1
    return NTERM

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
    
    mostrarG(G)
    TERM = calcularTerminables(G, V)
    mostrarTerminables(TERM)
