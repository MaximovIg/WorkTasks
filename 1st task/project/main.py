'''
Задание:

Напишите на библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. 
Дополнительно к работоспособности оценим:

-Юнит-тесты
-Легкость добавления других фигур
-Вычисление площади фигуры без знания типа фигуры в compile-time
-Проверку на то, является ли треугольник прямоугольным
'''

import figures


if __name__ == '__main__':
    square = figures.Circle(3.)
    triangle1 = figures.Triangle(3.5, 7., 5.3)
    triangle2 = figures.Triangle(3., 4., 5.)
    
    figures_list = []
    figures_list.append(square)
    figures_list.append(triangle1)    
    figures_list.append(triangle2) 

    for figure in figures_list:
        print(f'area of figure {figure} equals {figure.area():.2f}')
    
        