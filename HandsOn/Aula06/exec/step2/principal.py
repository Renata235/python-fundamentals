import psycopg2

flag = True

host = 'localhost'
dbname = 'projeto'
user = 'postgres'
password = '123456'

con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (host, dbname, user, password))
cur = con.cursor()

while flag:
    banner = '''Menu:
1) Logar
2) Cadastrar usuario
3) Lista usuario
4) Sair
Selecione a opcao: '''

    option = int(raw_input(banner))

    session = []

    if option == 1:
        user = raw_input('Username: ')
        pswd = raw_input('Password: ')

        query = "SELECT * FROM users WHERE usuario='%s' AND pass='%s'" % (user, pswd)
        cur.execute(query)

        usuario = cur.fetchone()

        if usuario:
            session.append(usuario)
        else:
            print 'Username ou password invalidos'
    elif option == 2:
        print 'Opcao 2 selecionada'
    elif option == 3:
        print 'Opcao 3 selecionada'
    elif option == 4:
        print 'Volte sempre'
        exit()
