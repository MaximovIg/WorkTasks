from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self) -> float:
        '''функция вычисления площади фигуры'''    

class Circle(Figure):
    
    def __init__(self, r: float):        
        if r < 0:
            raise ValueError('отрицательные значение недопустимы')
                
        self.r = r        
        
    def __repr__(self):
        return f'Circle({self.r})'    
    
    def area(self) -> float:
        return math.pi * math.pow(self.r, 2)       

class Triangle(Figure):

    def __init__(self, a: float, b: float, c: float):
        if a < 0 or b < 0 or c < 0:
            raise ValueError('отрицательные значение недопустимы')
        
        #проверяем что треугольник с такими сторонами в принципе может существовать
        if not (a + b >= c and b + c >= a and c + a >= b):
            raise ValueError('треугольник c такими сторонами не может существовать')
        
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c)/2.0 

    def __repr__(self):
        if self.is_right_angled():
            return f'Right-angled Triangle({self.a}, {self.b}, {self.c})'            
        else:
            return f'Triangle({self.a}, {self.b}, {self.c})'         

    def area(self) -> float:        
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))    
    
    # Не очень понял, что имелось в виду под пунктом "проверка на то, является ли треугольник прямоугольным..."
    # поэтому просто сделал отдельную функцию для этого"
    def is_right_angled(self) -> bool:
        return math.pow(self.a, 2) == math.pow(self.b, 2) + math.pow(self.c, 2) or \
               math.pow(self.b, 2) == math.pow(self.c, 2) + math.pow(self.a, 2) or \
               math.pow(self.c, 2) == math.pow(self.a, 2) + math.pow(self.b, 2)
       
