from ICalcMathABC import ICalcMathABC
import math
class Cercle(ICalcMathABC,Couleur):

    def __init__(self,rayon=0):
        self._rayon = rayon

    @property
    def rayon(self):
        return self._rayon
    
    @rayon.setter
    def rayon(self,rayon):
        self._rayon = rayon

    def __str__(self):
        return f"Cercle rayon : {self._rayon}"

    # def calc_surface(self):
    #     return math.pi*self._rayon**2
