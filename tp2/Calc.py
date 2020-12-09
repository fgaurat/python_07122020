from DivBy12Exception import DivBy12Exception


class Calc:


    def div(self,a,b):
        if b == 12:
            raise DivBy12Exception()
        return a/b