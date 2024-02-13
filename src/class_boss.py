import random
import pygame
import time
from clase_asteroides import *
from configuraciones import *
class Boss(pygame.sprite.Sprite):
    def __init__(self,tamanios, animaciones, posicion_inicial,  velocidad,es_visible):
        super().__init__()
        self.animaciones = animaciones
        self.tamanio =tamanios
        self.ancho = tamanios[0]
        self.alto = tamanios[1]
        self.reescalar_animaciones()
          # Cargar la imagen del boss
        self.es_visible = es_visible
        self.rectangulo = self.animaciones["boss_caminar"][0].get_rect()  # Definir el rectángulo
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo_boss(self.rectangulo)
        self.contador_pasos = 0
        self.velocidad = velocidad
        self.que_hace = "boss_quieto"
        self.direccion = 1
        self.ultimo_ataque = time.time()
        self.lista_ataques = ['ataque1', 'ataque2']  # Suponiendo tres tipos de ataques
        self.salud = 100  # Salud inicial del jefe
        self.ataque_actual = None
        self.direccion = 1
        self.posicion_inicial_x= 800
        self.posicion_final_x= 20
    
    def elegir_ataque(self):
        # Método para elegir un ataque de manera aleatoria
        self.ataque_actual = random.choice(self.lista_ataques)
        return self.ataque_actual
    def animar(self, pantalla, que_animacion):
        #Tiene que ir bliteando cad a una de las imagenes de la animacion con la que voy a trabajar
        #Ante cada evento(teclass) hay que animar al personaje
        #Necesito (self,pantalla, que_animacion:str - clave del diccionario que voy a sacar del objeto que me dice que animacion hay que ejectuar)
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], (self.rectangulo.x,self.rectangulo.y))
        self.contador_pasos += 1
    def reescalar_animaciones (self):
        #Diccionario de animaciones
        for clave in self.animaciones:
            for i in range (len(self.animaciones[clave])):
                self.animaciones[clave][i] =pygame.transform.scale(self.animaciones[clave][i],(self.ancho,self.alto))
    def caminar(self):
        for lado in self.lados:

            self.lados[lado].x += 10 * self.direccion
        if self.rectangulo.x < self.posicion_final_x:  
            self.direccion *= -1  # Cambia la dirección
            self.que_hace= "boss_derecha"
            
        elif self.rectangulo.x > self.posicion_inicial_x:
            self.que_hace = "boss_caminar"
            self.direccion *= -1
        
    
    def ejecutar_ataque(self):
        # Lógica específica para ejecutar el ataque actual
        if self.ataque_actual == 'ataque1':
            self.que_hace = "boss_ataque_uno"
            
        elif self.ataque_actual == 'ataque2':
            # Lógica para el ataque2
            self.que_hace = "boss_ataque_dos"
       

    
    def ataque_1(self):
        # Mover el jefe 10 píxeles
        self.mover_10_px()
        # Ejecutar animación de ataque
        self.que_hace = "boss_ataque_uno"

        

    def mover_10_px(self):
        # Mover el jefe 10 píxeles en la dirección actual
        # Suponiendo que 'direccion' es 1 para derecha y -1 para izquierda
        self.rectangulo.x -= 10 * self.direccion
    def ataque_dos(self,pantalla):
        self.que_hace = "boss_ataque_dos"
        self.lados["cabeza"].y -= 110
        
        
        
            

    def ejecutar_animacion_ataque(self,ataque):
        # Lógica para ejecutar la animación del ataque
        # Por ejemplo, cambiar el estado del jefe y llamar a un método de animación
        self.que_hace = ataque
        self.animar(self.que_hace)
    def actualizar(self, pantalla):
        if self.es_visible:
            self.animar(pantalla,self.que_hace)
            self.caminar()
            if self.debe_atacar():
                match self.elegir_ataque():
                    case "ataque1":
                        self.ataque_1()
                    case "ataque2":
                        self.ataque_dos(pantalla)
        
            

        
        # Decidir si es momento de atacar
        
        
        # ... (resto del método actualizar) ...

    def debe_atacar(self):
        # Comprobar si han pasado 5 segundos desde el último ataque
        tiempo_actual = time.time()
        if tiempo_actual - self.ultimo_ataque >= 5:
            self.ultimo_ataque = tiempo_actual
            return True
        return False

        
    def mover_izquierda(self):
        self.rect.x -=self.velocidad
        # Lógica para mover el boss
    
   
    #def actualizar(self,pantalla):
        
    def recibir_danio(self, cantidad):
        # Disminuir la salud cuando el boss recibe daño
        self.salud -= cantidad
        if self.salud <= 0:
            self.morir()

    

  
        # Más lógica de actualización según sea necesario