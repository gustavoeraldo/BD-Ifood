import sys

from db import db

'''
restaurante:
[x] Bustar comida 
[/] Buscar restaurante 
[x] Histórico de pedidos
[ ] Alterar perfil
'''

class Cliente():
  def __init__(self, cpf, nome, email, senha, telefone1, telefone2):
    self.cpf = cpf
    self.nome = nome
    self.email = email
    self.senha = senha
    self.telefone1 = telefone1
    self.telefone2 = telefone2

  def Alterar_Perfil(self):
    return 'Perfil alterado com sucesso'

  def Buscar_Comida(self):
    conn = db.Init_db()
    cur = conn.cursor()

    loop = True

    while loop:
      comida = input('Digite a comida que está procurando: ')

      if comida:
        cur.execute(f"""SELECT comida.nome, comida.preco, comida.codigo_comida, restaurante.nome FROM comida
        INNER JOIN restaurante ON comida.codigo_restaurante=restaurante.cnpj
        WHERE comida.nome ILIKE '{comida}%'""")
        
        resultado = cur.fetchall()

        if resultado:
          print("\t Comida \t\t Peço \t Restaurante\n")

          for item in resultado:
            nome, preco, _, restaurante = item
            print(f"\033[32m\t{nome}\033[37m \t R$ \033[33m {preco}\033[37m \t{restaurante} \n")

      opcao = input("""[ 1 ] - Continuar buscando comida
              [ 2 ] - Selecionar uma comida e fazer o pedido
              [ 3 ] - Voltar para o Menu\n""")

      if opcao == '1':
          pass
      elif opcao == '2':
        loop = self.Fazer_Pedido(conn, cur, resultado)
      elif opcao == '3':
        loop = False
      else: 
        pass

    db.Close_db(cur, conn)

    return 'lista de comidas'

  def Buscar_Restaurante(self):#Ajustar
    '''
    pesquisa o restaurante
    seleciona e olha o cardápio
    fazer pedido
    '''
    conn = db.Init_db()
    cur = conn.cursor()

    resultado=[]
    loop = True

    while loop:
      restaurante = input('\tDigite o restaurante que está procurando: ')

      if restaurante:
        cur.execute(f"SELECT nome, cnpj FROM restaurante WHERE nome ILIKE '{restaurante}%'")
        resultado = cur.fetchall()

        if resultado:
          print("\t Restaurantes\n")

          i = 0     
          for item in resultado:
            restaurante, _ = item
            print(f"\t \033[32m[{i}]\033[37m {restaurante}\n")
            i = i+1

      opcao = input("""[ 1 ] - Buscar por mais restaurantes
          [ 2 ] - Selecione o restaurante e visualize o cardápio
          [ 3 ] - Voltar para o Menu\n""")

      if opcao == '1':
        pass
      elif opcao == '2':
        # loop = self.Fazer_Pedido(conn, cur, resultado)
        indice = input('\tDigite o número do restaurante desejado: ')
        nome_restaurante, cnpj = resultado[int(indice)]

        cur.execute(f"""SELECT nome, preco, descricao FROM comida WHERE codigo_restaurante='{cnpj}';""")
        cardapio = cur.fetchall()

        print(f"""\t\t{'**'*12}*
        \t*\t \033[36m Cardápio \033[37m \t*
        \t{'**'*12}*\n""")

        print("\t Comida \t\t Peço")
        for comida in cardapio:
          nome, preco, descricao = comida
          print(f"\033[32m\t{nome}\033[37m \t R$ \033[33m {preco} \033[37m\n"
                f"\tContem: {descricao}"
          )

      elif opcao == '3':
        loop = False
      else: 
        pass

    db.Close_db(cur, conn)

    return 'buscar restaurante'

  def Cadastrar(self):
    conn = db.Init_db()
    cur = conn.cursor()

    try:
      cur.execute(f"INSERT INTO cliente VALUES ('{self.cpf}', '{self.nome}', '{self.email}', '{self.senha}', '{self.telefone1}', '{self.telefone2}');")
      conn.commit()
    except OSError as err:
      return f'Erro na criação do restaurante. {err}' 
    
    print('Usuário cadastrado com sucesso!')

    db.Close_db(cur, conn)
    return True

  def Fazer_Pedido(self, cur, conn, lista_comida):
    conn = db.Init_db()
    cur = conn.cursor()
    i = 0

    for item in lista_comida:
      comida, preco, _, restaurante = item
      print(f"\033[32m\t[{i}]{comida}\033[37m \t R$ \033[33m {preco}\033[37m \t{restaurante} \n")
      i = i+1

    index = input('Selecione a comida que irá pedir: ')
    comida, preco, cod_comida, restaurante = lista_comida[int(index)]

    quantidade = input('Digite a quantidade desejada do item selecionado: ')
    observacao = input('Informe observações extra: ')

    total = int(quantidade)*preco
    
    print(f'Informação do pedido: {comida} \t {round(total, 2)} \t {restaurante}')

    confirmacao = input('Deseja confirmar o pedido ?: (S/N)')

    if confirmacao.lower() == 's':
      try:
        cur.execute(f"""INSERT INTO pedido(total, quantidade_item, observacao, finalizado, codigo_cliente, codigo_comida)
        VALUES ({round(total, 2)},{quantidade},'{observacao}',{'false'},'{self.cpf}','{cod_comida}')""")
        conn.commit()
      except OSError as err:
        print(err)
        return f'{err}'
    elif confirmacao.lower() == 'n':
      print('\n\033[31m Pedido Cancelado!\033[37m\n')
      return True
     
    print('\n \033[32mPedido concluído com sucesso !\033[37m \n')
    db.Close_db(cur, conn)
    return True

  def Visualizar_Historico(self):
    conn = db.Init_db()
    cur = conn.cursor()
    
    try:
      cur.execute(f"""SELECT pedido.data_pedido, pedido.total, pedido.quantidade_item, comida.nome FROM pedido
      INNER JOIN comida ON pedido.codigo_comida=comida.codigo_comida WHERE pedido.codigo_cliente='{self.cpf}'""")

      historico = cur.fetchall()
    except OSError as err:
      print(err)
      return

    if historico:
      print("""\t\t\n********* HISTÓRICO DE PEDIDOS *********\n
      Data \t\t\t Comida \t\t Quantidade \t Total(R$)\n""")

      for item in historico:
        data, total, quantidade, comida = item
        print(f"* {data} \t \033[32m{comida}\033[37m \t {quantidade} \t\t R$\033[33m{total}\033[37m")
    else: 
      print('Nenhum pedido realizado\n')

    db.Close_db(cur, conn)
    return True

  def Ver_Cardápio():
    return True