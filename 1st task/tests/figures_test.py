import unittest
import math

from project import figures


class CircleTest(unittest.TestCase):

    def test_area_right(self):
        #правильный результат
        r = 5.
        circle = figures.Circle(r)

        self.assertEqual(circle.area(), r*r*math.pi)

    def test_area_wrong(self):
        #неправильный результат
        r = 6.
        circle = figures.Circle(r)
        
        self.assertNotEqual(circle.area(), 5.*5.*math.pi)

    def test_exception(self):
        #отрицательные входные данные    
        with self.assertRaises(ValueError):
            circle = figures.Circle(-5.)


class TriangleTest(unittest.TestCase):

    def test_area(self):
        #правильный результат
        a = 4.3
        b = 11.2
        c = 8.45 
        p = (a + b + c)/2
        triangle = figures.Triangle(a, b, c) 
        
        self.assertEqual(triangle.area(), math.sqrt(p * (p - a) * (p - b) * (p - c)))

    def test_area_neg(self):
        #правильный результат
        a = 4.3
        b = 11.2
        c = 8.45 
        p = (a + b + c)/2
        triangle = figures.Triangle(a, b, c)        
        
        self.assertNotEqual(triangle.area(), math.sqrt(p * (p - 5.) * (p - b) * (p - c)))  

    def test_exception1(self):
        #отрицательные входные данные     
        with self.assertRaises(ValueError):
            a = 4.3
            b = -11.2
            c = 8.45 
            p = (a + b + c)/2
            triangle = figures.Triangle(a, b, c)

    def test_exception2(self):
        #треугольник с такими сторонами не может существовать 
        with self.assertRaises(ValueError):
            a = 4.3
            b = 13.2
            c = 8.45 
            p = (a + b + c)/2
            triangle = figures.Triangle(a, b, c)
            
    def test_is_right_angled(self):
        #правильный результат
        a = 2.1
        b = 2.8
        c = 3.5 
        triangle = figures.Triangle(a, b, c) 

        self.assertTrue(triangle.is_right_angled())  


    def test_is_right_angled_neg(self):
        #неправильный результат   
        a = 2.1
        b = 2.5
        c = 3.5 
        triangle = figures.Triangle(a, b, c) 
        
        self.assertFalse(triangle.is_right_angled())    




