def area(a, b, c):
    ''' Возвращает полупериметор треугольника 

            Параметры:
                a (int, float) - первая переменная
                b (int, float) - вторая переменная
                c (int, float) - третья переменная
                
            Возвращаемое значение:
                pol_per(int, float): полупериметор треугольника
    '''
    return (a + b + c) / 2


def perimeter(a, b, c):
    ''' Возвращает либо сумму, либо строку  

            Параметры:
                a (int, float, string) - первая переменная
                b (int, float, string) - вторая переменная
                c (int, float, string) - третья переменная

            Возвращаемое значение:
                perimeter(int, float): периметр треугольника
                либо
                a + b + c(string): строка
    '''
    return a + b + c
