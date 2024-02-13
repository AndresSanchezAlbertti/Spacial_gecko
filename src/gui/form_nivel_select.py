import pygame
from manejador_niveles import *
from pygame.locals import *
from gui.GUI_form_contenedor_niveles import *
from gui.GUI_button import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_label import *
from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_form_menu_score import *
class FormNivelSelect(Form):
    def __init__(self, screen, x,y,w,h,color_background="black", color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        ##COMPLETAR
        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()

        pygame.mixer.music.load("Recursos/Vengeance (Loopable).wav")

        pygame.mixer.music.set_volume(self.volumen)

        pygame.mixer.music.play(-1)


        self.boton_nivel_1 = Button_Image(self._slave, x, y, 255, 50, 300, 100, onclick= self.entrar_nivel,
                                          onclick_param= "nivel_uno",
                                          path_image="Recursos/play_game.png")
        self.boton_nivel_2 = Button_Image(self._slave, x, y, 255, 150, 300, 100,onclick= self.entrar_nivel,
                                          onclick_param= "nivel_dos",
                                          path_image="Recursos/options.png")
        #self.boton_nivel_3 = Button_Image(self._slave, x, y, 50, 90, 50, 50,onclick= self.entrar_nivel,
        #                                  onclick_param = "nivel_uno",
        #                                  path_image="Recursos/Menu_BTN.png" )
        
    
        self.lista_widgets.append(self.boton_nivel_1)
        self.lista_widgets.append(self.boton_nivel_2)
        #self.lista_widgets.append(self.boton_nivel_3)
        self.render()


    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                #self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = formContenedorNivel(self._master,nivel
                                                ) 
        self.show_dialog(form_contenedor_nivel)
 
    def btn_tabla_click(self, param):
        diccionario = [{"Jugador": "Gio", "Score": 5}, {"Jugador": "Vani", "Score": 3}, {"Jugador": "Marcos", "Score": 7}]

        nuevo_form = FormMenuScore(screen = self._master,
                                   x = 250, y = 25,
                                   w = 500, h = 550,
                                   color_background = (220, 0, 220),
                                   color_border = (0, 0, 0),
                                   active = True,
                                   path_image = "Recursos\Window.png",
                                   scoreboard = diccionario,
                                   margen_x = 50,
                                   margen_y = 100,
                                   espacio = 30)


        self.show_dialog(nuevo_form)