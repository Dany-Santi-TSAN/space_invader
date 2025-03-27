import pygame, sys


class Alien(pygame.sprite.Sprite):    #pygame.sprite.Sprite: des fonctionnalités prédéfinies pour les sprites dans Pygame
    def _init_(self,color,x,y): #Sélection des paramètres
        super()._init_() #s'assurer que tout est correctement configuré pour un sprite
        alien_path = f'png/alien_image/{color}_invader.png' #Crée un chemin vers l'image de l'alien
        self.image = pygame.image.load(alien_path).convert_alpha() #pygame.image.load(file_path) = Charge l'image depuis le chemin spécifié - .convert_alpha() : Gère la transparence de l'image, pour que les parties transparentes soient bien rendues.
        self.rect = self.image.get_rect(topleft = (x,y)) #Crée un rectangle (un cadre de coordonnées) autour de l'image de l'alien - Topleft: Place le coin supérieur gauche de l'image à la position (x, y).
