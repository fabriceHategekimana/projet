from options import *

#Pour invoquer cette fonction dans la classe principale, il suffit de faire drawDialog(self.window, "Hello world!") par exemple.
#La particularité de ce code est que le texte est arrangé pour ne pas dépasser du cadre

def drawDialog(surface, text, aa=False, bkg=None):
    rect= pygame.draw.rect(surface, (0, 0, 0), (0, 400, 1000, 200))
    font = pygame.font.Font(pygame.font.match_font('arial'), 20)
    color = (255, 255, 255)
    y = rect.top
    lineSpacing = -2

    #Le code qui suit sert à ajuster le texte pour qu'il ne dépasse pas de la boite
    """Nous donne la taille du font"""
    fontHeight = font.size("Tg")[1]
    while text:
        i = 1
        """détermine si la ligne du texte va être en dehors de la zone de texte"""
        if y + fontHeight > rect.bottom:
            break
        """détermine la largeur maximum de la zone de texte"""
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
        """si on coupe la ligne, on coupe depuis le dernier mot complet sur la ligne"""     
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
        """écrit la ligne et la colle à la surface"""
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
        """retire le texte que nous venons tout juste de coller"""
        text = text[i:]

    return text
