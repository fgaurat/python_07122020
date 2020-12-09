from abc import ABCMeta,abstractmethod 

class ICalcMathABC(metaclass=ABCMeta):

    @abstractmethod
    def calc_surface(self):
        pass