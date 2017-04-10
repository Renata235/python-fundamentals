import sys
from datetime import datetime

datetime().strftime()


def erro(msg):
    print "Erro:", msg
    sys.exit(1)


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def quadrado(x):
    return x ** 2

if __name__ == "__main__":
    print inc(10) # deve mostrar 11
    print dec(10) # deve mostrar 9
    print quadrado(5) # deve mostrar 25ex