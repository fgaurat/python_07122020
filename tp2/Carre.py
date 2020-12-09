from RectangleP import RectangleP


class Carre(RectangleP):

    def __init__(self,cote=0):
        super().__init__(cote,cote)
        print("def __init__(self,cote=0):")
        self._cote = cote

    @property
    def cote(self):
        return self._cote
    
    @cote.setter
    def cote(self,cote):
        self._cote = cote

    def __str__(self):
        return f"Carre cote : {self._cote}"
