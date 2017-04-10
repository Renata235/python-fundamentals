# ----- CONEXAO COM O BANCO
import psycopg2

con = psycopg2.connect(
    "host=%s dbname=%s user=%s password=%s" % (
    'localhost', 'projeto', 'postgres', '123456'
    )
)

cur = con.cursor()
# ----- INSERIR UM POST
# RECEBE conteudo e titulo
conteudo = raw_input('Digite o conteudo: ')
titulo = raw_input('Digite o titulo: ')

cur.execute("INSERT INTO posts(conteudo, titulo) \
VALUES('%s', '%s')" % (conteudo, titulo))
con.commit()
# ----- BUSCAR UM POST
# RECEBE trecho do titulo
# trecho = raw_input('Digite um texto para busca: ')
id = raw_input('Digite o id busca: ')

cur.execute("SELECT * FROM posts \
WHERE id=%s" % id)

row = cur.fetchone()

print "ID %s | TITULO %s | CONTEUDO %s" % (
    row[0], row[1], row[2]
)
