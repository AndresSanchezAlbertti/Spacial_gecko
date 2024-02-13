import pygame
from pygame.locals import *

from gui.GUI_button import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_label import *
from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_form_menu_score import *

class formContenedorNivel(Form):
    def __init__(self,pantalla,nivel):
        super().__init__(pantalla, 0,0, pantalla.get_width(),pantalla.get_height())
        nivel._slave = self._slave
        self.nivel = nivel

    def update(self,lista_eventos):
        self.nivel.update(lista_eventos)
        self.draw()