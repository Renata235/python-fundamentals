# animais = ['tigre', 'boi', 'galinha']
#
# b = 'a'
#
# def exibir_lista(lista):
#     b = 's'
#     for a in lista:
#         print a
# #
# exibir_lista(animais)
# #
# def somar(a=8, b=2):
#     return a+b
# #
# a = int(raw_input('Valor a: '))
# b = int(raw_input('Valor b: '))
# resultado = somar(a, b)
# #
# print resultado
#
#     #-----------
# def subtrair(*args):
#     saida = ''
#     for a in args:
#         saida =  saida + str(a)
#     print saida
#
# subtrair(2,3,10,50)
#
# def multiplicar(*args,**kwargs):
#     print kwargs
#     print args
#
# multiplicar(2, 3, a=2, b=1, c=4, d=6)
#
#     #---------
# f = lambda x,y,z: x + y + z
# print f(2,3,4)
#
# words = ['pera', 'uva', 'mamao']
#
# def size(words):
#     lista = []
#     for e in words:
#         lista.append(len(e))
#     return lista
#
# frutas = lambda words: [len(w) for w in words]
#
# print frutas(words)
def func(valor):
    if valor:
        raise Exception('Deu ruim!')
    #----------
try:
    print 'primeira linha'
    func(True)
    print 3 + 3
except Exception as e:
    print e
finally:
    print 'sempre executa'
