import os
import pygame

_image_library = {}

#Fonction pour l'image
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        pygame.transform.scale(image, (110, 110))
        _image_library[path] = image
    return image

#Fonction pour le son
def get_sound_name(path):
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    return canonicalized_path