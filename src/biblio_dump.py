

piso = Plataforma("piso.png",0,(0,300, W,20))
piso.top = player.lados["main"].bottom
lados_piso = piso.lados
#en sprites van a estar tdoos los elementos del juego
sprites = pygame.sprite.Group()
sprites.add(player)
#En enemigos van a ir todos los sprites de enemigos
enemigos = pygame.sprite.Group()
#plataforma
numero_plataformas = 4
espacio_entre_plataformas = 50
# Calcula el ancho disponible para las plataformas (restando el espacio entre ellas)
ancho_disponible = W - (numero_plataformas - 1) * espacio_entre_plataformas
# Calcula el ancho de cada plataforma
ancho_plataforma = W / numero_plataformas
rectangulos_plataformas = []
# Calcula las coordenadas x de cada plataforma
plataforma_uno=Plataforma("plataforma_wood.png",5,(W-700,H - 100))
plataforma_dos = Plataforma("plataforma_wood.png",5,(W-750,(H/2) +150))
plataforma_tres = Plataforma("plataforma_wood.png",5,(W-600,(H/2) +120))
plataformasw_1 = [
                  plataforma_uno,
                  plataforma_dos,
                  plataforma_tres
                 ]
plataformasw_1_rec = [plataforma_uno.imagen, plataforma_dos.imagen,plataforma_tres.imagen]

plataformas_lados  = []

piso_grande_uno =  pygame.Rect(0,590,W-200,30)
piso_grande_dos = pygame.Rect(240,200,W - 830,30)
piso_grande_tres = pygame.Rect(350,0,W -700,30 )
piso_grande_cuatro= pygame.Rect(540,200,W - 720,30)

plataformas_lados = [piso.lados,plataforma_uno.lados,plataforma_dos.lados,plataforma_tres.lados]
pisos_grandes = [piso_grande_uno,piso_grande_dos,piso_grande_tres,piso_grande_cuatro]
 lista_coordenadas = [(800,300), (200,50), (40,50),(150,500),(300,450)]
    lista_coordenadas_w = [((W-700,H - 75)),(W-750,(H/2) +200),(W-600,(H/2) +100)]
    numero_plataformas_w = 3
    
    pantalla.fill("Black")
    
    pantalla.blit(fondo,(0,0))
    
    
    rectangulos_plata =[]
    for i in range(numero_plataformas_w):

        for i in lista_coordenadas_w:
            
            y = i[0]
            x = i[1]
            for plataforma in plataformas_wood:
                pantalla.blit(plataforma.imagen,(x,y))
                


                #plataforma.mover_plataforma()
for i in pisos_grandes:
    plataformas_lados.append(i)

if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top +5
            
        else:
            self.esta_saltando = True



lista_coordenadas_w = [((W-700,H - 75)),(W-750,(H/2) +200),(W-600,(H/2) +100)]
    numero_plataformas_w = 3
    pantalla.fill("Black")
    pantalla.blit(fondo,(0,0))
    pantalla.blit(piso_sprite,(-100,540))
    rectangulos_plata =[]
    for i in range(numero_plataformas_w):

        for i in lista_coordenadas_w:
            
            y = i[0]
            x = i[1]
            for plataforma in plataformas_wood:
                pantalla.blit(plataforma.imagen,(y,x))
                #plataforma.mover_plataforma()

#mover plataformas:
if un_personaje.lados["bottom"].colliderect(plataforma_movediza.lados["top"]):
            plataforma_movediza.posicion_y = plataforma_movediza.posicion_y - 5     
            un_personaje.posicion_y = un_personaje.posicion_y -5
