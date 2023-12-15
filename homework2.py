def function1(*args, **kwargs):
    suma = 0
    if len(kwargs) == 0 and len(args) == 0:
        return 0
    for i in args:
        if type(i) is int or type(i) is float:
            suma += i

    # for i, value in kwargs.items():
    #     if type(value) is int or type(value) is float:
    #         suma += value
    return suma


print(f'Suma numerelor reale sou intregi este', function1(1, 5, -3, "abc", [12, 56, "cad"]))
print(function1())
print(f'Suma numerelor reale sou intregi este', function1(2, 4, "abc", param_1=2))


def function2(lista1):
    if not lista1:
        return 0, 0, 0
    a, b, c = function2(lista1[1::])
    a += lista1[0]
    b += lista1[0] if lista1[0] % 2 == 0 else 0
    c += lista1[0] if lista1[0] % 2 == 1 else 0
    return a, b, c


lista = [5, 4, 3, 2, 8, 6, 4, 21]
a, b, c = function2(lista)
print(f'Suma totala: {a}, Suma numerelor pare: {b}, Suma numerelor impare: {c}')


def function3():
    nr = input("Introduceti un numar intreg:")
    try:
        return int(nr)
    except ValueError:
        return 0


print(function3())
