
from ICalcMath import ICalcMath

class RectangleP(ICalcMath):

    _cpt = 0

    def __init__(self,longueur=0,largeur=0):
        print("def __init__(self,longueur=0,largeur=0)")
        self._longueur = longueur
        self._largeur = largeur
        RectangleP._cpt+=1

    def __str__(self):
        return f"Rectangle : longueur : {self._longueur}, largeur : {self._largeur}"
    
    def hasDict(self):
        return {'longueur':self._longueur,'largeur':self._largeur}

    @property
    def longueur(self):
        print("get longueur")
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,longueur):
        print("set longueur")
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,a):
        self._largeur = a

    @staticmethod
    def get_cpt():
        return RectangleP._cpt

    def calc_surface(self):
        return self._largeur*self._longueur

    # longueur= property(fget=get_longueur,fset=set_longueur)
    # largeur= property(fget=get_largeur,fset=set_largeur)