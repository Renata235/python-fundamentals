import psycopg2

con = psycopg2.connect(
    "host=%s dbname=%s user=%s password=%s" % (
    'localhost', 'projeto', 'postgres', '123456'
    )
)

cur = con.cursor()
    #----------- SELECT
cur.execute("SELECT * FROM posts")

for row in cur.fetchall():
    print 'ID: %s \nTitulo: %s\n Conteudo: %s' % (
        row[0], row[1], row[2]
    )

row = cur.fetchone():
print 'ID: %s \nTitulo: %s\n Conteudo: %s' % (
    row[0], row[1], row[2]
)
    #----------- INSERT UPDATE DELETE
try:
    cur.execute(" \
    INSERT INTO posts(conteudo, titulo) \
    VALUES('%s', '%s')" % ('Meu COnteudo', 'Titulo'))

    if cur.rowcount:
        print 'Registro inserido com sucesso!'
        con.commit()
except Exception as e:
    print e
    con.rollback()
