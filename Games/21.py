import random

# La variable almacena el monto minimo de la apuesta.
ap_min = 5000
# la lista guarda el valor de todas las cartas posibles en el juego.
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Se define la clase Jugador
class Jugador:
    # Metodo constructor de la clase Jugador
    def __init__(self, nombre, apuesta):
        # Se inicializan los valores por defecto cuando se crea una instancia
        # Almacena el nombre del jugador
        self.nombre = nombre
        # Almacena el monto de la apuesta.
        self.apuesta = apuesta
        # La lista guarda instancias de la clase Carta
        self.cartas = []
    
    # Metodo que cambia el valor de la variable apuesta de la clase Jugador
    def setApuesta(self, monto):
        self.apuesta = monto
    
    # El método devuelve al valor de la apuesta del jugador.
    def getApuesta(self):
        return self.apuesta
    
    # El método devuelve el nombre del jugador.
    def getNombre(self):
        return self.nombre
        
    # Este método agrega una carta a lista de cartas que tiene el jugador en la mano.
    def nuevaCarta(self, carta):
        self.cartas.append(carta)
    
    # Este método devuelve la cantidad de cartas que tiene el jugador en la mano.
    def getNumCartas(self):
        return len(self.cartas)
    
    # Este método devuelve un array que contiene las cartas del jugador.
    def getCartas(self):
        return self.cartas

# Se define la clase carta
class Carta:
    # Método contructor de la clase Carta
    def __init__(self):
        # Se inicializa la variable miembro valor con un valor aleatorio entre 0 y 12.
        self.valor = random.randint(0, 12)
    
    # Este metodo devuelve la representación de la carta
    def getCarta(self):
        return cartas[self.valor]
     
    # Este metodo devuelve el valor de la carta
    def getValor(self):
        return self.valor

# Se define la clase Juego
class Juego:
    # Método constructor de la clase
    def __init__(self, nombre, apuesta):
        # Crea una instancia de la clase jugador llamada player
        self.player = Jugador(nombre, apuesta)
    
    # Este método cambia el monto apostado por el jugador,
    # llama al método setApuesta de la instancia player
    def setApuesta(self, apuesta):
        self.player.setApuesta(apuesta)
        
    # Este método devuelve el monto apostado por el jugador,
    # llama al método getApuesta de la instancia player.
    def getApuesta(self):
        return self.player.getApuesta()
    
    # Este método devuelve el nombre del jugador, llama al método
    # getNombre() de la instancia player.
    def getNombre(self):
        return self.player.getNombre()
    
    # Este método pide las primeras dos cartas para iniciar el juego.
    def pedirCartas(self):
        for i in range(2):
            self.player.nuevaCarta(Carta())
    
    # Pedir una nueva carta y agregarla a la mano del jugador.
    def otraCarta(self):
        self.player.nuevaCarta(Carta())

    # Este método muestra las cartas del jugador.
    def verCartas(self):
        for i in range(self.player.getNumCartas()):
            print(" +-----+\n",
                "| ",self.player.getCartas()[i].getCarta()," |\n",
                "|  ", "  |\n",
                "+-----+\n")

    # Realizar el calculo con el valor de las cartas.
    def calcJuego(self):
        total = 0
        as_t = 0
        # Primero sumamos todas las cartas que no sean A
        for i in range(self.player.getNumCartas()):
            c = self.player.getCartas()[i].getCarta()
            if (c == 'J' or c == 'Q' or c == 'K'):
                total += 10
            elif (c == 'A'):
                as_t += 1
            else:
                total += int(c)
        
        # Evaluamos para todas las A cual debe ser su valor       
        if (as_t != 0):
            for i in range(as_t):
                if ( total + 11  > 21 ):
                    total += 1
                else:
                    total += 11
        return total

# Este método lee el monto de la apuesta y verifica que sea mayor o igual al 
# minimo permitido para jugar.
# Por último retorna el valor leido y verificado.
def obtenerApuesta():
    while True:
        cantidad = int(input("Cuanto dinero quiere apostar?\t"))
        if ( cantidad >= ap_min ):
            break
        else:
            print("Debes apostar como minimo $", str(ap_min), " pesos.")
    return cantidad

# Leer el nombre del jugador y almacenarlo en nombre.
nombre = input("Cual es el nombre del jugador?\t")
# Leer el monto de la apuesta y almacenarlo en apuesta .
apuesta = obtenerApuesta()
# Crea una instancia de la clase Juego.
veintiuna = Juego(nombre, apuesta)
# Pedir las primeras dos cartas.
veintiuna.pedirCartas()
while True:
    # Mostrar las cartas del jugador
    veintiuna.verCartas()
    # Preguntar si las cartas suman menos de 21
    if ( veintiuna.calcJuego() < 21 ):
        # Preguntar si quiere sacar otra carta, si es asi, aumenta la puesta por el minimo.
        otra_carta = input("Pedir otra carta (s/n)? (debe incrementar la apuesta por el minimo)")
        if (otra_carta == 's'):
            veintiuna.setApuesta(veintiuna.getApuesta() + ap_min)
            veintiuna.otraCarta()
        # Si no aumenta la apuesta y pide carta, el jugador pierde.
        else:
            print(veintiuna.getNombre(), " pierde todo.")
            break;
    # Si se pasa de Veintiuno el jugador pierde.
    elif ( veintiuna.calcJuego() > 21 ):
        print(veintiuna.getNombre(), " pierde todo.")
        break;
    # Si tiene Veintiuno el jugador gana el juego y se lleva el doble de lo que apostó.
    else:
        print("Ganaste ", veintiuna.getNombre(), "!!")
        print("Te llevas $", str(veintiuna.getApuesta() * 2), " pesos.")
        break;

