def valores(*args, **kwargs):
    print type(args)
    print type(kwargs)

valores('a', 'b', 'c')

    #-------- lambda
f = lambda x, y, z: x + y + z
print f(2, 3, 4)

words = ['look', 'so', 'car', 'ice', 'melted']

def size_each(words):
    return [len(w) for w in words]
print size_each(words)

size_each = lambda words: [len(w) for w in words]
print size_each(words)

    #-------- TRY
def func(a):
    if a:
        raise Exception('Valor invalido')

try:
    func()
except Exception as e:

    print 'Algum problema aconteceu'
finally:
    prinr 'Executa esse bloco'
