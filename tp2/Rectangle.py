

class Rectangle:

    cpt = 0

    def __init__(self,longueur,largeur):
        self._longueur = longueur
        self._largeur = largeur
        Rectangle.cpt+=1
    
    def __str__(self):
        return f"Rectangle : longueur : {self._longueur}, largeur : {self._largeur}"


    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self,longueur):
        self._longueur = longueur

    def set_largeur(self):
        self._largeur = largeur