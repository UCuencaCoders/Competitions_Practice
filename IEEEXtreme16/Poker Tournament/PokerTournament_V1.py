import numpy as np


# Functions
def type0(a, l, r, c):
    a[l : r + 1] = c
    return a


def type1(a, l, r, c):
    a[l : r + 1] = np.maximum(a[l : r + 1], c)
    return a


def type2(a, l, r, k):
    global acotada, maximo

    suma_final.clear()
    acotada = a[l : r + 1]

    # Filtrar los ceros
    acotada = acotada[acotada != 0]
    acotada.sort()

    maximo = len(acotada) - 1
    desplazador = k - 1

    res = sumatoria(0, maximo - desplazador)
    print(np.uint32(res))


def sumatoria(inicial, final):
    if final == maximo:
        sub_array = acotada[inicial : final + 1]
        res = suma_final.get(
            (inicial, final),
            None,
        )

        if res is None:
            suma_final[(inicial, final)] = np.uint32(np.sum(sub_array)) % 998244353
            return suma_final[(inicial, final)]

        return res

    else:
        return (
            np.uint32(
                np.sum(
                    [
                        (acotada[i] * sumatoria(i + 1, final + 1)) % 998244353
                        for i in range(inicial, final + 1)
                    ]
                )
            )
            % 998244353
        )


# Globals
suma_final = {}


# Main
if __name__ == "__main__":
    n, q = map(np.uint16, input().split())

    a = np.array(list(map(int, input().split())), dtype=np.uint32)

    for _ in range(q):
        op, l, r, c = list(map(int, input().split()))

        match op:
            case 0:
                a = type0(a, l, r, c)
            case 1:
                a = type1(a, l, r, c)
            case 2:
                type2(a, l, r, c)
