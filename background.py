import image as img
import pygame

class Background():
    def __init__(self, imageNames, screen):
        self.screen = screen    # screen sur lequelle background est affiché
        self.images = []
        for imageName in imageNames:
            currentImage = pygame.transform.scale(img.get_image(imageName), (1024, 768))
            self.images.append(currentImage)
        self.lengthX = 0        # X de la largeur cumulé des images de images[]
        for image in self.images:
            self.lengthX += image.get_size()[0]
        self.firstImageX = 0
        self.mooveSpeed = 3


    def display(self):
        # affiche les images de images[] en ligne avec la 1ere image a gauche
        if self.firstImageX + self.lengthX <= 1024:  # Si le bout de la liste d'image va etre visible au prochain update
            self.firstImageX = self.firstImageX + self.images[0].get_size()[0]
            self.images = self.images[1:] + [self.images[0]]

        x = self.firstImageX
        for index, img in enumerate(self.images):
            self.screen.blit(img, (x, 0))
            x += img.get_size()[0]

    def update(self):
        self.firstImageX = self.firstImageX - self.mooveSpeed

    def setMooveSpeed(self, ms):
        self.mooveSpeed = ms


