from math import *

class MyCustomException(Exception):
    pass

def decorator(uscorenie):
    def obertka(v_start, v_end, t):
        a = (v_start - v_end) // t
        s = (v_end * t) + (a*pow(t, 2)/2)
        try:
            uscorenie(int(input()), int(input()), int(input()))
        except (MyCustomException, ValueError):
            print("Данные должны быть числами!!")
            print(f"Возникла ошибка: {e}")
        print(s)
    return obertka

@decorator
def uscorenie(v_start, v_end, t):
    if t == 0:
        raise MyCustomException("t не может быть равно 0")
    a = (v_start - v_end) // t
    print(a)

print(uscorenie(int(input()), int(input()), int(input())))



