import pygame
import image as img
from background import Background

pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("WYPU")
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_icon(img.get_image('assets/petitlogo.png'))

# importer arrière plan
background = Background(['assets/backgroundv2.png', 'assets/backgroundv2.png'], screen)


# variable pour le reglement
get_rules = True
# afficher le reglement
def rules():
    black = (0, 0, 0)
    font = pygame.font.Font(None, 30)
    rules_title = font.render("RÈGLES DU JEU : ", True, black)
    rules1 = font.render("- Attrappez les bons fruits et légumes qui sont dans la liste en haut à gauche de l'écran ", True, black)
    rules2 = font.render("pour cela déplacez le joueur à l'aide des touches directionnelles de votre clavier", True, black)
    rules3 = font.render("afin d'augmenter votre score et de maintenir votre energie qui baisse en fonction du temps, si", True, black)
    rules4 = font.render("vous attrapez un mauvais fruit ou légumes votre score va baisser, votre énergie, si", True, black)
    rules5 = font.render("elle est entièrement consommée, vous fera perdre une vie et vous endormiras, vous devez", True, black)
    rules6 = font.render("spamer la touche espace pour pouvoir vous réveiller, et recommencer, au bout de 3 barres ", True, black)
    rules7 = font.render("d'énergie, soit 3 vie, vous aurez perdus.", True, black)
    if get_rules:
        screen.blit(rules_title, (450, 40))
        screen.blit(rules1, (80, 100))
        screen.blit(rules2, (80, 135))
        screen.blit(rules3, (80, 170))
        screen.blit(rules4, (80, 205))
        screen.blit(rules5, (80, 240))
        screen.blit(rules6, (80, 275))
        screen.blit(rules7, (80, 310))


# creer une classe qui represente le jeu
class Home:

    def __init__(self):
        # définir si le jeu a commencé ou pas
        self.is_playing = False
        # generer le joueur
        self.j = Joueur()
        self.pressed = {}
        self.play = pygame.image.load('assets/play.png')
        self.play = pygame.transform.scale(self.play, (256, 128))
        self.quit = pygame.image.load('assets/quit.png')
        self.quit = pygame.transform.scale(self.quit, (256, 128))
        self.settings = pygame.image.load('assets/settings.png')
        self.settings = pygame.transform.scale(self.settings, (320, 128))


# creer une classe pour le joueur
class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.points_de_vie = 100
        self.max_points_de_vie = 100
        self.attaque = 10
        self.vitesse_de_deplacement = 1
        self.image = pygame.image.load('assets/character.png')
        self.image = pygame.transform.scale(self.image, (70, 102))
        self.position = self.image.get_rect()
        self.position.x = 400
        self.position.y = 500

    def deplacement_droite(self):
        self.position.x += self.vitesse_de_deplacement

    def deplacement_gauche(self):
        self.position.x -= self.vitesse_de_deplacement

background.display()
# charger Page d'acceuil
home = Home()

fenetre_ouverte = True

while fenetre_ouverte:
    # On récupère la valeur de l'input
    pressed = pygame.key.get_pressed()

    # mettre l'arrière plan

    screen.blit(home.j.image, home.j.position)

    # affichage des boutons
    screen.blit(home.play, (62, 610))
    screen.blit(home.settings, (362, 610))
    screen.blit(home.quit, (726, 610))


    # verifier si le joueur va à gauche ou à droite
    if home.pressed.get(pygame.K_RIGHT) and home.j.position.x + home.j.position.width < screen.get_width():
        home.j.deplacement_droite()
    elif home.pressed.get(pygame.K_LEFT) and home.j.position.x > 0:
        home.j.deplacement_gauche()

    # maj ecran
    pygame.display.flip()

    # si l'utilisateur ferme la fenetre
    for evenement in pygame.event.get():
        # si l'evenement est la fermeture de la fenetre
        if evenement.type == pygame.QUIT:
            fenetre_ouverte = False
            pygame.quit()
            print("Jeu Fermé")

        # si l'evenement => lacher une touche du clavier
        elif evenement.type == pygame.KEYDOWN:
            home.pressed[evenement.key] = True

        elif evenement.type == pygame.KEYUP:
            home.pressed[evenement.key] = False

        # verifie que la touche entrée est pressed et que le joueur est au dessus du bouton correcpondant
        if pressed[pygame.K_RETURN]:
            if home.j.position.x > 62 and home.j.position.x < 256:
                print("commencer le jeu")
                # exécute le fichier game.py du projet the dire

            elif home.j.position.x > 362 and home.j.position.x < 682:
                print("afficher settings")
                get_rules = True
                rules()
            elif home.j.position.x > 726 and home.j.position.x < 982:
                print("quitter jeu")
                fenetre_ouverte = False
                pygame.quit()
        elif home.j.position.x > 362 and home.j.position.x < 682 and pressed[pygame.K_BACKSPACE]:
            print("effacer settings")
            background.display()
