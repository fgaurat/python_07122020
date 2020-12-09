

class Rectangle:

    cpt = 0

    def __init__(self,longueur=0,largeur=0):
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

    def set_largeur(self,a):
        self._largeur = a


    longueur= property(fget=get_longueur,fset=set_longueur)
    largeur= property(fget=get_largeur,fset=set_largeur)