import os

def creartablaTransiciones(transiciones):
    tabla_t = {}
    tabla_i = {}
    
    for t in transiciones:
        l = t.split(',')
        
        ki = l[1][0]
        vi = int(l[1][-1])
        e = {ki : vi}
        tabla_i.update(e)
        
        kt = int(l[0][-1])
        d = {kt : tabla_i.copy()}
        
        tabla_t.update(d)
    
    return tabla_t

def validarCaracter(alfabeto, estado, tabla_t, caracter):
    if( caracter in alfabeto ):
        return tabla_t[estado][caracter]
    return -1
        
def SimuladorAFD(alfabeto, estado_inicial, estados_aceptacion, tabla_t, test_case):
    estado = estado_inicial
    if (test_case == "" or test_case == "&") and 0 in estados_aceptacion:
            estado = 0
    else:
        for caracter in test_case:
            estado = validarCaracter(alfabeto, estado, tabla_t, caracter)

    if estado in estados_aceptacion:
        return "ACEPTADA"
    else:
        return "RECHAZADA"
        
if __name__ == '__main__':
    
    alfabeto = list(input().rstrip().split())
    
    estados = []
    for j in list(input().rstrip().split()):
        estados.append(int(j[-1]))
    
    estado_inicial = int(input()[-1])
    
    estados_aceptacion = []
    for i in list(input().rstrip().split()):
        estados_aceptacion.append(int(i[-1]))
    
    transiciones = list(input().rstrip().split())
        
    # Creamos la tabla de transiciones
    tabla_t = creartablaTransiciones(transiciones)

    n_inputs = int(input())
    
    for i in range(n_inputs):
        try:
            cadena = input()
        except:
            cadena = ""

        print( SimuladorAFD(alfabeto, estado_inicial, estados_aceptacion, tabla_t, cadena ) )
        
        estado_inicial = 0
