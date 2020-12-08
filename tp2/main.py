#!/usr/bin/env python
from Rectangle import Rectangle

def main():
    r = Rectangle(1,2)
    print(Rectangle.cpt)
    r1 = Rectangle(11,12)
    print(Rectangle.cpt)
    r1.set_longueur(-12)
    
    print(f"longueur {r.get_longueur()}, largeur {r.get_largeur()}")
    print(f"longueur {r1.get_longueur()}, largeur {r1.get_largeur()}")

    print("r",r)

if __name__ == "__main__":
    main()

