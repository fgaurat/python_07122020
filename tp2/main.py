#!/usr/bin/env python
from Rectangle import Rectangle
from RectangleP import RectangleP
from Carre import Carre
from Cercle import Cercle
from ICalcMath import ICalcMath
from Calc import Calc
from DivBy12Exception import DivBy12Exception

def showSurface(o):
    print("def showSurface(o):")
    print(o)
    print(o.calc_surface())

def main():
    # r = Rectangle(1,2)
    # print(Rectangle.cpt)
    # r1 = Rectangle(11,12)
    # print(Rectangle.cpt)
    # r1.set_longueur(-12)
    
    # print(f"longueur {r.get_longueur()}, largeur {r.get_largeur()}")
    # print(f"longueur {r1.get_longueur()}, largeur {r1.get_largeur()}")

    # print("r",r)
    # r = Rectangle(1,2)
    # r.longueur = 12
    # r.set_largeur(12)
    # l = r.get_largeur()

    # r.longueur=14
    # a =  r.longueur
    # # r.set_longueur(14)
    
    # print(r.longueur)
    # # print((r.get_longueur())
    # rp = RectangleP(1,2)
    # print(rp.longueur)
    # rp.longueur=15
    # print(rp.longueur)
    # print(RectangleP.get_cpt())
    # print(rp.calc_surface())
    # rp = RectangleP(1,2)
    # c = Carre(2)
    ce = Cercle(2)
    print(Cercle.__mro__)
    # print(ce)
    # showSurface(rp)
    # showSurface(c)
    showSurface(ce)
    # calc = Calc()

    # try:
    #     c = calc.div(1,12)
    #     print(c)
    # # except ZeroDivisionError as e:
    # #     print("erreur",e)
    # except DivBy12Exception as e:
    #     print("DivBy12Exception erreur",e)
    #     raise Exception()
    # finally:
    #     print("après erreur")



if __name__ == "__main__":
    main()
