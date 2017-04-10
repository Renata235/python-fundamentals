flag = True

while flag:
    banner = '''Menu:
1) Logar
2) Cadastrar usuario
3) Lista usuario
4) Sair
Selecione a opcao: '''

    option = int(raw_input(banner))

    if option == 1:
        print 'Opcao 1 selecionadda'
    elif option == 2:
        print 'Opcao 2 selecionada'
    elif option == 3:
        print 'Opcao 3 selecionada'
    elif option == 4:
        print 'Volte sempre'
        flag = False
