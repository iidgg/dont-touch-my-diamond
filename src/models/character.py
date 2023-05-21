import pygame
import src.utils.constants as C
from src.models.objs.animated import animatedObject

class Character(animatedObject):
    def __init__(self):
        animatedObject.__init__(self)