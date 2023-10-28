
import os
import random
from readchar import readkey, key

class Juego:
    posini = (0,0)
    posfin = (0,0)
    mapa = None
    pasillo = '.'
    pared = '#'
    jugador = 'P'
    
    def __init__(self):
        juego_archivo = JuegoArchivo()
        self.mapa = juego_archivo.getMapa()
        self.posfin = ( (len( self.mapa ) - 1) , (len( self.mapa[0] ) -1) )
        self.moverJugador(self.posini[0], self.posini[1])

    def limpiarPantalla(self):
        os.system('cls')

    def movimientoValido(self, x, y):
        if (x, y) >= self.posini or (x, y) < self.posfin:
            return True
        return False
    
    def esPasillo(self, x, y):
        if self.mapa[x][y] == self.pasillo:
            return True
        return False

    def esPared(self, x, y):
        if self.mapa[x][y] == self.pared:
            return True
        return False
    
    def moverJugador(self, row, col):
        pos_jugador = self.posJugador()        
        if self.movimientoValido(row, col) == True:
            if self.esPasillo( row, col ) == True:
                self.mapa[pos_jugador[0]][pos_jugador[1]] = self.pasillo
                self.mapa[row][col] = self.jugador

            elif self.esPared( row, col ):
                self.mapa[pos_jugador[0]][pos_jugador[1]] = self.jugador
                

    def posJugador(self):
        pos_jugador = (0,0)
        for i in range( len( self.mapa ) ):
            for j in range( len( self.mapa[i] ) ):
                if( self.mapa[i][j] == self.jugador ):
                    pos_jugador = (i,j)
                    break
        return pos_jugador
    
    def btnMovimiento(self, x, y):
        print( 'movimientos ← ↑ ↓ → ')       
        print( 'Posicion Jugador: ', self.posJugador(),'nueva pos:',x,y, 'salida', self.posfin )
        
        k = readkey()        
        if k == key.UP:
            x -= 1
        elif k == key.DOWN:
            x += 1
        elif k == key.LEFT:
            y -= 1
        elif k == key.RIGHT:
            y += 1

        self.moverJugador( x, y )

    def mostrarMapa(self):
        self.limpiarPantalla()
        print( 'Proyecto integrador Parte 5\n\tEncapsulando el juego en una clase')
        print('================================================================')
        print( '\t para realizar los movimientos precione las Teclas ← ↑ ↓ → ')
        print('================================================================')
        for i in range( len(self.mapa) ):
            for j in range( len(self.mapa[i]) ) :
                print( self.mapa[i][j], end="" )
            print()
        print('\n================================================================')   

    def main(self):
        px,py = self.posJugador()
        while (px,py) < self.posfin:            
            self.mostrarMapa()
            self.btnMovimiento(px, py)
            px,py = self.posJugador()
        self.mostrarMapa()
        print('================================================================')
        print('Felicidades as terminado el laverinto!!!!')    
            

class JuegoArchivo:
    mapa = None
    path_completo = None
    def __init__(self):
        self.generarMapa()
        self.cargarMapa()
       
    def generarMapa(self):
        self.path_completo = f"{'mapas'}/{random.choice( os.listdir('./mapas') )}"
    
    def cargarMapa(self):
        archivo = open(self.path_completo, "r")
        self.mapa = archivo.readlines()    
        for row in range( len(self.mapa) ):
            self.mapa[row] = list( (self.mapa[row]).strip() )    
        archivo.close()
    
    def getMapa(self):
        return self.mapa
    

juego = Juego()
juego.main()