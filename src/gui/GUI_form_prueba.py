import pygame
from pygame.locals import *

from gui.GUI_button import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_label import *
from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_form_menu_score import *
from gui.form_nivel_select import *


class FormPrueba(Form):
    def __init__(self, screen, x,y,w,h,color_background="black", color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)

        ##COMPLETAR
        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()

        pygame.mixer.music.load("Recursos/Vengeance (Loopable).wav")

        pygame.mixer.music.set_volume(self.volumen)

        pygame.mixer.music.play(-1)

        self.txt_nombre = TextBox(self._slave, 
                                  x, y,
                                  50, 50,
                                  150, 30,
                                  "gray", "white", "red", "blue", 2,
                                  font = "Comic Sans", font_size = 15,
                                  font_color = "black")

      

        self.boton_play = Button_Image(self._slave, x, y, 255, 50, 300, 100,
                                        "Recursos/play_game.png", self.btn_niveles_click, "")
        self.boton_option = Button_Image(self._slave, x, y, 255, 150, 300, 100,
                                        "Recursos/options.png", self.btn_tabla_click, "")
        self.boton_score = Button_Image(self._slave, x, y, 50, 90, 50, 50,
                                        "Recursos/Menu_BTN.png", self.btn_tabla_click, "")
        
        




        self.lista_widgets.append(self.txt_nombre)
        #self.lista_widgets.append(self.boton_play)
        #self.lista_widgets.append(self.slider_volumen)
        #self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.boton_option)
        self.lista_widgets.append(self.boton_score)



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

    #def update_volumen(self, lista_eventos):
        #self.volumen = self.slider_volumen.value
        #self.label_volumen.update(lista_eventos)
        #self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        #pygame.mixer.music.set_volume(self.volumen)
        
        

    #def btn_play_click(self, param):
    #    if self.flag_play:
    #        pygame.mixer.music.pause()
    #        self.boton_play._color_background = "cyan"
    #        self.boton_play.set_text("Play")
    #    else:
    #       pygame.mixer.music.unpause()
    #       self.boton_play._color_background = "red"
    #       self.boton_play.set_text("Pause")
    #    self.flag_play = not self.flag_play
    
    def btn_tabla_click(self, param):
        diccionario = [{"Jugador": "Gio", "Score": 5}, {"Jugador": "Vani", "Score": 3}, {"Jugador": "Marcos", "Score": 7}]

        nuevo_form = FormMenuScore(screen = self._master,
                                   x = 250, y = 25,
                                   w = 500, h = 550,
                                   color_background = "black",
                                   color_border = (0, 0, 0),
                                   active = True,
                                   path_image = "Recursos\Window.png",
                                   scoreboard = diccionario,
                                   margen_x = 50,
                                   margen_y = 100,
                                   espacio = 30)


        self.show_dialog(nuevo_form)
    
    def btn_niveles_click(self, param):
        nuevo_form = FormNivelSelect(
            self._master,  # Pasa la pantalla principal o el "master" como primer argumento
            x=0,  # Proporciona las coordenadas x, y, ancho y alto según sea necesario
            y=0,
            w=self._master.get_width(),
            h=self._master.get_height(),
            color_background="black",  # Proporciona el color de fondo deseado
        # Otras opciones personalizadas aquí...
    )
        self.show_dialog(nuevo_form)