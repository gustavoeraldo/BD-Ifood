import sys
import datetime

from db import db

class Cliente():
  def __init__(self, cpf, nome, email, senha, telefone1, telefone2):
    self.cpf = cpf
    self.nome = nome
    self.email = email
    self.senha = senha
    self.telefone1 = telefone1
    self.telefone2 = telefone2

  def Buscar_Comida(self):
    conn = db.Init_db()
    cur = conn.cursor()

    resultado = []
    loop = True

    while loop:
      comida = input("""
      Digite a comida que está procurando
      (Apenas clique Enter para mais opções): """)

      if comida:
        cur.execute(f"""SELECT comida.nome, comida.preco, comida.codigo_comida, restaurante.nome, 
        restaurante.entrega FROM comida INNER JOIN restaurante ON 
        comida.codigo_restaurante=restaurante.cnpj WHERE comida.nome ILIKE '{comida}%'""")
        
        resultado = cur.fetchall()

        if resultado:
          print("\t Comida \t\t Peço \t Restaurante \t Frete")

          for item in resultado:
            nome, preco, _, restaurante, frete = item
            print(f"\033[32m\t{nome}\033[37m \t R$ \033[33m {preco}\033[37m \t{restaurante} \t {frete}\n")

      opcao = input("""
        [ 1 ] - Continuar buscando comida
        [ 2 ] - Selecionar uma comida e fazer o pedido
        [ 3 ] - Voltar para o Menu
        -> """)

      if opcao == '1':
        pass
      elif opcao == '2' and resultado:
        loop = self.Fazer_Pedido(resultado)
      elif opcao == '3':
        loop = False
      else: 
        pass

    db.Close_db(cur, conn)

    return 'lista de comidas'

  def Buscar_Restaurante(self):#Ajustar
    '''
    [ ] Restaurante Popular
    '''
    conn = db.Init_db()
    cur = conn.cursor()

    resultado=[]
    loop = True

    while loop:
      restaurante = input("""
      Digite o restaurante que está procurando
      (Apenas clique Enter para mais opções): """)

      if restaurante:
        cur.execute(f"SELECT nome, cnpj FROM restaurante WHERE nome ILIKE '{restaurante}%';")
        resultado = cur.fetchall()

        if resultado:
          self.Resultado_Pesquisa(resultado)

      opcao = input("""
      [ 1 ] - Buscar por restaurantes
      [ 2 ] - Ver todos os restaurantes
      [ 3 ] - Ver todos os restaurantes com entrega grátis
      [ 4 ] - Ver todos os restaurantes populares
      [ 5 ] - Selecione o restaurante e visualize o cardápio
      [ 6 ] - Voltar para o Menu
      -> """)

      if opcao == '1':# Buscar por mais restaurantes
        pass

      elif opcao == '2':
        cur.execute('SELECT nome, cnpj FROM restaurante;')
        resultado = cur.fetchall()
        self.Resultado_Pesquisa(resultado, 'Restaurantes')

      elif opcao == '3':
        cur.execute('SELECT nome, cnpj FROM restaurante WHERE entrega=0;')
        resultado = cur.fetchall()
        self.Resultado_Pesquisa(resultado, 'Restaurantes com Entrega grátis')

      elif opcao == '5':
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

      elif opcao == '6':
        loop = False
      else: 
        pass

    db.Close_db(cur, conn)

    return True

  def Cadastrar(self):
    conn = db.Init_db()
    cur = conn.cursor()

    try:
      cur.execute(f"INSERT INTO cliente VALUES ('{self.cpf}', '{self.nome}', '{self.email}', '{self.senha}', '{self.telefone1}', '{self.telefone2}');")
      conn.commit()
    except OSError as err:
      raise Exception (f"{err}")
    
    print('Usuário cadastrado com sucesso!')

    db.Close_db(cur, conn)
    return True

  def Fazer_Pedido(self, lista_comida):
    conn = db.Init_db()
    cur = conn.cursor()
    i = 0

    for item in lista_comida:
      comida, preco, _, restaurante, frete = item
      print(f"\033[32m\t[{i}]{comida}\033[37m \t R$ \033[33m {preco}\033[37m \t{restaurante} \t R$ {frete}\n")
      i = i+1

    index = input('Selecione a comida que irá pedir: ')
    try:
      comida, preco, cod_comida, restaurante, frete = lista_comida[int(index)]
    except Exception as e:
      print('Seleção de inválida')

    quantidade = input('Digite a quantidade desejada do item selecionado: ')
    observacao = input('Informe observações extra: ')

    total = int(quantidade)*preco
    
    print(f'Informação do pedido: {comida} \t Total: R$ {round(total, 2)+frete} \t Do {restaurante} com frete de R${frete}')

    confirmacao = input('Deseja confirmar o pedido ?: (S/N)')

    if confirmacao.lower() == 's':
      try:
        cur.execute(f"""INSERT INTO pedido(total, quantidade_item, observacao, finalizado, codigo_cliente, codigo_comida)
        VALUES ({round(total, 2)},{quantidade},'{observacao}',{'false'},'{self.cpf}','{cod_comida}') 
        RETURNING pedido.data_pedido, pedido.codigo_pedido;""")
        data, cod_pedido = cur.fetchone() 
        conn.commit()

        cur.execute(f"""INSERT INTO item_pedido (preco_comida, data_pedido, codigo_pedido, codigo_comida)
        VALUES ({preco}, '{data}', {cod_pedido}, )""")
        conn.commit()
      except Exception as e:
        print(f'Erro na requisição do pedido. {e}')
        return True

    elif confirmacao.lower() == 'n':
      print('\n\033[31m Pedido Cancelado!\033[37m\n')
      return True
     
    print('\033[32mPedido concluído com sucesso !\033[37m \n')
    db.Close_db(cur, conn)
    return True

  def Visualizar_Historico(self):# Histórico de pedidos
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
      print("""
        \033[33m******************* HISTÓRICO DE PEDIDOS *******************\033[37m
        Data \t\t\t Comida \t Quantidade \t Total(R$)
        """)

      for item in historico:
        data, total, quantidade, comida = item
        print(f"* {data} \t \033[32m{comida}\033[37m \t {quantidade} \t R$\033[33m {total}\033[37m")
    else: 
      print('\t Nenhum pedido realizado\n')

    db.Close_db(cur, conn)
    return True

  # Funções para exibir resultado de pesquisa de restaurantes
  def Resultado_Pesquisa(self, resultado, titulo):
    print(f"\n\t {titulo}\n")

    i = 0     
    for item in resultado:
      restaurante, _ = item
      print(f"\t \033[32m[{i}] - \033[37m {restaurante}\n")
      i = i+1

