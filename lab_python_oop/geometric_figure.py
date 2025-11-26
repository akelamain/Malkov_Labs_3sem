from abc import ABC, abstractmethod

class GeometricFigure(ABC):    
    def __init__(self):
        self.name = self.__class__.__name__
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    def get_name(self):
        return self.name