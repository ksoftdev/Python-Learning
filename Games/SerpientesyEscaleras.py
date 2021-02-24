import random

# Bandera, para saber cuando termina el juego.
ganador = False
 
# Se define la clase tablero.
class Tablero:

    # Método constructor de la clase Tablero.
    def __init__(self):
        # Creamos un diccionario llamado escaleras que guarda las escaleras que
        # tiene el tablero.
        # Las escaleras se representan en el tablero como + (inicio) y : (fin)
        self.escaleras = {2:22,6:35,12:32,39:59,46:55,79:82,92:99}
        # Creamos un diccionario llamado serpientes que guarda las serpientes
        # que tiene el tablero.
        # Las serpientes se representan en el tablero como - (inicio) y ; (fin) 
        self.serpientes = {98:76,95:86,89:52,74:56,56:45,49:27,36:14,17:3}
        # Un lista que guarda el tablero de juego.
        self.tabla = [ x for x in range(100, 0 ,-1) ]
    
    # Este método verifica si el diccionario serpientes tiene una clave n, si 
    # la tiene le asiga a n el valor de la clave, si no, simplemente retorna 
    # el valor recibido.
    def verificarSerpientes(self, n):
        # Si serpientes tiene una clave n...
        if n in self.serpientes:
            # Muestre este mensaje
            print ("Es una serpiente, bajas!!")
            # Asigne a n el valor de la clave
            n = self.serpientes[n]
        # Retorne n
        return n

    # Este método verifica si el diccionario escaleras tiene una clave n, si la
    # tiene le asiga a n el valor de la clave, si no, simplemente retorna el 
    # valor recibido.
    def verificarEscaleras(self, n):
        # Si escaleras tiene una clave n...
        if n in self.escaleras:
            # Muestre este mensaje
            print ("Es una escalera, subes!!")
            # Asigne a n el valor de la clave
            n = self.escaleras[n]
        # Retorne n
        return n

    # Devuelve la lista que guarda el tablero de juego.
    def getTabla(self):
        return self.tabla
            
# Se define la clase Dado
class Dado:
    # Método contructor de la clase Dado
    def __init__(self):
        # Se inicializa la variable miembro valor con un valor aleatorio entre 1 y 6.
        self.valor = random.randint(1, 6)
    
    # Este metodo lanza el dado.
    def lanzar(self):
        # Da un nuevo valor aleatorio al dado.
        self.valor = random.randint(1, 6)
    
    # Este método devuelve el valor del dado.
    def getValor(self):
        return self.valor
        
# Se define la clase jugador
class Jugador:

    # Método constructor de la clase Jugador
    def __init__(self, nombre, ficha):
        # Asigna al posicion el valor 0 (Inicio)
        self.posicion = 0
        # Asigna el nombre al jugador desde el valor recibido
        self.nombre = nombre
        # Un simbolo que representa la ficha del jugador en el tablero de juego.
        self.ficha = ficha
    
    # Este método define la nueva posición del jugador.
    def setPosicion(self, posicion):
        self.posicion = posicion
    
    # Este método devuelve el nombre del jugador
    def getNombre(self):
        return self.nombre
        
    # Este método devuelve la posicion actual del jugador.
    def getPosicion(self):
        return self.posicion
    
    # Devuelve la ficha del jugador
    def getFicha(self):
        return self.ficha

# Se define la clase jugador
class Juego:

    # Método constructor de la clase Juego
    def __init__(self, nombre_j1, nombre_j2):
        # Se crea el jugador #1 (Objeto de la clase Jugador).
        self.jugador1 = Jugador(nombre_j1, "*P1*")
        # Se crea el jugador #2 (Objeto de la clase Jugador).
        self.jugador2 = Jugador(nombre_j2, "*P2*")
        # Se crea una instancia de la clase tablero.
        self.tablero = Tablero()

    # Este método retorna la instancia jugador1
    def getJ1(self):
        return self.jugador1
    
    # Este método retorna la instancia jugador2 
    def getJ2(self):
        return self.jugador2
    
    # Llamada al método verificarSerpientes de la clase Tablero, con n como 
    # argumento.
    def verificarSerpientes(self, n):
        return self.tablero.verificarSerpientes(n)
        
    # Llamada al método verificarEscaleras de la clase Tablero, con n como
    # argumento.
    def verificarEscaleras(self, n):
        return self.tablero.verificarEscaleras(n)
        
    # Este método muestra el tablero de juego en pantalla.
    def verTablero(self):
        # Un recorrido desde 0, de 10 en 10, hasta 90, para mostrar las filas
        # del tablero, ya que este es una lista unidimensional de 100 elementos.
        for i in range(0, 91, 10):
            # Se crear una sublista de 10 elementos para representar una fila
            lst = self.tablero.getTabla()[i:i+10]
            # Si es una fila par...
            if int(i/10) % 2 == 1:
                # Mostramos los elementos de forma inversa.
                lst.reverse()
                
            # Recorremos la sub-lista elemento pot elemento.
            for i in lst:
                # Verificamos en que posicion se encuentra cada uno de los 
                # jugadores y los mostramos en el tablero.
                if ( i == self.jugador1.getPosicion() ):
                    # Usamos end en la funcion print para no terminar la linea
                    # hasta que se encuentre una cadena vacia.
                    print(self.jugador1.getFicha(), "\t", end="")
                elif ( i == self.jugador2.getPosicion() ):
                    print(self.jugador2.getFicha(), "\t", end="")
                # Si no es la posicion del jugador muestra el numero correspondiente
                # del tablero.
                else:
                    # Iteramos en el diccionario escaleras, para marcar las escaleras
                    # en el tablero de juego.
                    for clave, valor in self.tablero.escaleras.items():
                        if i == clave:
                            print("+", end="")
                        elif i == valor:
                            print(":", end="")
                    # Iteramos en el diccionario serpientes, para marcar las serpientes
                    # en el tablero de juego.
                    for clave, valor in self.tablero.serpientes.items():
                        if i == clave:
                            print("-", end="")
                        elif i == valor:
                            print(";", end="")
                    print(i, "\t", end="")
            # "Imprimimos" una cadena vacia, para iniciar en una nueva linea.
            print("", "\n")

# Inicia el programa...
# Se piden los nombres a los jugadores.
nomj1 = input("Nombre del jugador 1:\t")
nomj2 = input("Nombre del jugador 2:\t")

# Se crea una instancia de la clase Juego...
sye = Juego(nomj1, nomj2)

# Se crea una instancia de la clase Dado...
dado = Dado()

# Este realiza las acciones que tienen lugar en el turno de un jugador,
# rebice como parámetro una instancia de Jugador
def jugarTurno(Jugador):
    # Turno Jugador
    # Pide el nombre del jugador, espera que se presione ENTER para continuar...
    print("\n\nTurno de", Jugador.getNombre())
    input("Presiona la tecla ENTER para lanzar el dado...")
    # Guardamos en pos la posicion inicial del jugador antes de iniciar el turno.
    pos = Jugador.getPosicion()
    # lanzamos el dado
    dado.lanzar()
    # Mostramos en pantalla el valor del lanzamiento.
    print("Tu lanzamiento fue: ", dado.getValor())
    # Actualizamos la posicion del jugador.
    Jugador.setPosicion(Jugador.getPosicion() + dado.getValor())
    # Verificamos si la nueva posicion es una serpiente y se actualiza la
    # posicion.
    Jugador.setPosicion(sye.verificarSerpientes(Jugador.getPosicion()))
    # Verificamos si la nueva posicion es una escalera y se actualiza la
    # posicion.
    Jugador.setPosicion(sye.verificarEscaleras(Jugador.getPosicion()))
    # Muestra el total de casillas recorridas, lanzamiento + o - serpientes y 
    # escaleras.
    print("Te moviste ", Jugador.getPosicion() - pos, " casillas.\n\n")

# Mientras que no haya un ganador, continua el juego.
while not ganador:

    # Mostrar el tablero.
    sye.verTablero()
    
    # Turno Jugador 1
    jugarTurno(sye.getJ1())
    
    # Turno Jugador 2
    jugarTurno(sye.getJ2())

    # Si terminado el turno la posicion de alguno de los jugadores es mayor o
    # igual que 100, entonces, termina el juego.
    if ( sye.getJ1().getPosicion() >= 100 ):
        print("\n\nEl ganador es ", sye.getJ1().getNombre(), "!!!")
        ganador = True
    elif ( sye.getJ2().getPosicion() >= 100 ):
        print("\n\nEl ganador es ", sye.getJ2().getNombre(), "!!!")
        ganador = True
     
