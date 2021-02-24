import random

jugar = True
min_apuesta = 1000
min_inicial = 5000

class Jugador:
    def __init__(self, bolsa, desc, nombre):
        self.bolsa = bolsa
        self.desc = desc
        self.nombre = nombre
        self.aciertos = 0
        self.apuesta = 0
        
    def setAciertos(self, aciertos):
        self.aciertos = aciertos
        
    def getAciertos(self):
        return self.aciertos

    def setApuesta(self, monto):
        self.apuesta = monto
        
    def getApuesta(self):
        return self.apuesta
        
    def sumarABolsa(self, cantidad):
        self.bolsa += cantidad
        
    def restarABolsa(self, cantidad):
        self.bolsa -= cantidad
        
    def getDesc(self):
        return self.desc
        
    def getNombre(self):
        return self.nombre
        
    def getBolsa(self):
        return self.bolsa
        
class Dado:
    def __init__(self):
        self.valor = random.randint(1, 6)
    
    def lanzar(self):
        self.valor = random.randint(1, 6)

    def getValor(self):
        return self.valor
    
class Juego:
    def __init__(self, bolsa, bolsa_j1, nombre_j1, bolsa_j2, nombre_j2):
        self.bolsa = bolsa
        self.jugador1 = Jugador(bolsa_j1, '', nombre_j1)
        self.jugador2 = Jugador(bolsa_j2, '', nombre_j2)
        self.Dado1 = Dado()
        self.Dado2 = Dado()
        self.Dado3 = Dado()
        self.Dado4 = Dado()
        
    def getJ1(self):
        return self.jugador1
        
    def getJ2(self):
        return self.jugador2
        
    def getD1(self):
        return self.Dado1
        
    def getD2(self):
        return self.Dado2
        
    def getD3(self):
        return self.Dado3
        
    def getD4(self):
        return self.Dado4

    def getBolsa(self):
        return self.bolsa
          
    def sumarABolsa(self, cantidad):
        self.bolsa += cantidad
        
    def restarABolsa(self, cantidad):
        self.bolsa -= cantidad

    def lanzarDados(self):
        self.getD1().lanzar()
        self.getD2().lanzar()
        self.getD3().lanzar()
        self.getD4().lanzar()
        
        print("\nlanzamiento: ",
            str(self.getD1().getValor()), " ",
            str(self.getD2().getValor()), " ",
            str(self.getD3().getValor()), " ",
            str(self.getD4().getValor()))

    def getAciertos(self, p):
        a = 0
        if ( self.getD1().getValor() == p ):
            a += 1
        if ( self.getD2().getValor() == p ):
            a += 1
        if ( self.getD3().getValor() == p ):
            a += 1
        if ( self.getD4().getValor() == p ):
            a += 1
        return a
        
    def stats(self):
        print("+-------------------------------------------------+\n",
            "Casa\t\t",
            self.getJ1().getNombre(),"\t\t",
            self.getJ2().getNombre(),"\n",
            "$",str(self.getBolsa()),
            "\t$",str(self.getJ1().getBolsa()),
            "\t$",str(self.getJ2().getBolsa()), "\n"         
            "+-------------------------------------------------+\n")

    def calcular(self, jug):
        if ( jug.getAciertos() == 4 ):
            jug.sumarABolsa(jug.getApuesta())
            self.restarABolsa(jug.getApuesta())
        elif ( jug.getAciertos() == 3 ):
            jug.sumarABolsa(0)
            self.restarABolsa(0)
        elif ( jug.getAciertos() == 2 ):
            jug.restarABolsa(int(jug.getApuesta()/2))
            self.sumarABolsa(int(jug.getApuesta()/2))
        elif ( jug.getAciertos() <= 1 ):
            jug.restarABolsa(jug.getApuesta())
            self.sumarABolsa(jug.getApuesta())

def getPred():
    while True:
        prediccion = int(input("Cual sera el resultado del lanzamiento?\t"))
        if ( prediccion > 0 and prediccion <= 6 ):
            break
        else:
            print("EL numero debe estar entre 1 y 6")
    return prediccion

def getApta():
    while True:
        apuesta = int(input("Cuanto dinero apuesta en esta ronda?\t"))
        if ( apuesta >= min_apuesta ):
            break
        else:
            print("La apuesta minima son $",str(min_apuesta)," pesos.")
    return apuesta

def getAptaInicial():
    while True:
        monto = int(input("Con cuanto dinero quiere jugar?\t"))
        if ( monto >= min_inicial ):
            break
        else:
            print("Para jugar debe apostar minimo $", str(min_inicial), "pesos.")
    return monto

nj1 = input("Nombre del jugador 1?\t")
bj1 = getAptaInicial()
nj2 = input("Nombre del jugador 2?\t")
bj2 = getAptaInicial()

dados = Juego(bj1 + bj2, bj1, nj1, bj2, nj2)

while jugar:
    print("\nComienza la ronda\n")
    dados.stats()
    # Turno Jugador 1
    print("Turno de", dados.getJ1().getNombre())
    dados.getJ1().setApuesta(getApta())
    prediccion = getPred()
    dados.lanzarDados()
    dados.getJ1().setAciertos(dados.getAciertos(prediccion))
    print("Aciertos:\t", dados.getJ1().getAciertos(), "\n")
    
    # Turno Jugador 2
    print("Turno de", dados.getJ2().getNombre())
    dados.getJ2().setApuesta(getApta())
    prediccion = getPred()
    dados.lanzarDados()
    dados.getJ2().setAciertos(dados.getAciertos(prediccion))
    print("Aciertos:\t", dados.getJ2().getAciertos(), "\n")
    
    dados.calcular(dados.getJ1())
    dados.calcular(dados.getJ2())
    
    if ( dados.getJ1().getBolsa() == 0 or dados.getJ1().getBolsa() < min_apuesta ):
        print(dados.getJ1().getNombre(), " pierde.\n")
        jugar = False
    elif ( dados.getJ2().getBolsa() == 0 or dados.getJ2().getBolsa() < min_apuesta ):
        print(dados.getJ2().getNombre(), " pierde.\n")
        jugar = False
    elif ( dados.getBolsa() == 0 ):
        print("Termina el juego.\n", "El ganador es ")
        if ( dados.getJ1().getBolsa() > dados.getJ2().getBolsa() ):
            print(dados.getJ1().getNombre(), "\n")
        else:
            print(dados.getJ2().getNombre(), "\n")
        jugar = False
       
