import sys
import random

from db import db

class Restaurante:
  def __init__(self, cnpj, email, senha, nome, entrega, aberto ):
    self.cnpj = cnpj
    self.email = email
    self.senha =senha
    self.nome = nome
    self.entrega = entrega
    self.aberto = aberto
  
  def Cadastrar(self):
    conn = db.Init_db()
    cur = conn.cursor()

    try:
      cur.execute(f"""INSERT INTO restaurante VALUES
      ('{self.cnpj}', '{self.email}', '{self.senha}', '{self.nome}', {self.entrega}, '{self.aberto}');""")
      conn.commit()
    except Exception as err:
      raise Exception (f'Erro no cadastro do restaurante. {err}') 
    
    print('Restaurante cadastrado com sucesso!')
    db.Close_db(cur, conn)
    return True

  def Atualizar_Cardapio(self):
    loop = True

    while loop:
      opcao = input('[ 1 ] - Adicionar comida\n'
              '[ 2 ] - Editar comida\n'
              '[ 3 ] - Deletar comida\n'
              '[ 4 ] - Voltar para o menu\n')

      if opcao == '1':
          loop = self.Adicionar_Comida()
      elif opcao == '2':
        loop = self.Editar_Comida()
      elif opcao == '3':
        loop = self.Deletar_Comida()
      elif opcao == '4':
          loop = False

    return True

  def Adicionar_Comida(self):

    conn = db.Init_db()
    cur = conn.cursor()
    
    nome = input('Digite o nome da comida (máximo de 25 caracteres):\n') 
    preco = input('Digite o preco da comida:\n') 
    descricao = input('Digite o descrição da comida (máximo de 100 caracteres):\n')  

    try:
      cur.execute(f"""INSERT INTO comida(nome, preco, descricao, codigo_restaurante) 
      VALUES ('{nome}', {float(preco)}, '{descricao}', '{self.cnpj}');""")
      conn.commit()
    except Exception as err:
      print(f'Ocorreu um erro na adição de comida.')
      raise Exception (f'{err}')

    print('\033[32m Comida adicionada com sucesso! \033[37m')

    db.Close_db(cur, conn)
    return True
    
  def Deletar_Comida(self):
    conn = db.Init_db()
    cur = conn.cursor()

    self.Visualizar_Cardapio()
    comida = input('Digite o nome da comida que deseja deletar:\n')
   
    try:
      cur.execute(f"DELETE FROM comida WHERE nome='{comida}' AND codigo_restaurante='{self.cnpj}'")  
      conn.commit()
    except Exception as err:
      print(err)
      return f'{err}'

    print('\033[32m Comida deletada com sucesso! \033[37m')
    
    db.Close_db(cur, conn)
    return True

  def Editar_Comida(self):
    conn = db.Init_db()
    cur = conn.cursor()

    self.Visualizar_Cardapio()
    antiga_comida = input('Digite o nome da comida que deseja alterar: \n')
    novo_nome = input('Digite o novo nome da comida: \n')
    novo_preco = float(input('Digite o novo preço da comida: \n'))

    try:
      cur.execute(f"""UPDATE comida SET nome='{novo_nome}', preco={round(novo_preco, 2)} 
      WHERE nome='{antiga_comida}' AND codigo_restaurante='{self.cnpj}';""")  
      conn.commit()
    except Exception as err:
      print(err)
      raise Exception (f'{err}')
    
    print('\033[32m Comida Editada com sucesso! \033[37m')
    db.Close_db(cur, conn)
    return True

  def Visualizar_Cardapio(self):#Atualizar visualização
    conn = db.Init_db()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM comida WHERE codigo_restaurante='{self.cnpj}';" )
    cardapio = cur.fetchall()
    
    if cardapio:
      print(f"""
      *******************\033[36m CARDÁPIO \033[37m *******************
      """)

      print("\t Comida \t\t Peço")
      for comida in cardapio:
        _, nome, preco, descricao, _ = comida

        print(f"""
        \033[32m{nome}\033[37m \t R$ \033[33m {preco} \033[37m
        Contem: {descricao}
        """)
    else:
      print('\033[33m\t Nenhuma comida foi adicionada no seu cardápio !!\033[37m')
  
    db.Close_db(cur, conn)
    return True

  def Obter_relatorio(self):# Apresenta um menu com os tipos de relatório
    loop = True

    while loop:
      print("""
      *******************\033[36m RELATÓRIOS \033[37m *******************""")

      opcao = input("""
      \033[36m[ 1 ]\033[37m - Obter relatório da comida mais vendida
      \033[36m[ 2 ]\033[37m - Obter relatório de todas as vendas
      \033[36m[ 3 ]\033[37m - Preço médio das comidas vendidas
      \033[36m[ 4 ]\033[37m - Voltar para o Menu
      -> """)

      if opcao == '1':
        loop = self.Comida_Mais_Vendidas()
      elif opcao == '2':
        loop = self.Historico_Vendas()
      elif opcao == '3':
        loop = self.Media_Preco_Vendas()
      elif opcao == '4':
        loop = False

    return True

  def Comida_Mais_Vendidas(self):
    conn = db.Init_db()
    cur = conn.cursor()

    cur.execute(f"""SELECT SUM(pedido.quantidade_item) as total, comida.nome FROM comida 
    INNER JOIN pedido ON comida.codigo_comida=pedido.codigo_comida 
    WHERE comida.codigo_restaurante='{self.cnpj}' 
    GROUP BY comida.nome ORDER BY total DESC;""")
    
    relatorio = cur.fetchall()
    if relatorio:
      print(f"""
      *******************\033[36m Relatório: Comida mais vendida \033[37m *******************""")

      comida, quantidade = relatorio[0]
      print(f"""
      Comida \t\t\t Quantidade
      {comida} \t {quantidade}
      """)
    else:
      print(f"""
      \033[33m Não há nenhum cadastro de vendas! \033[37m
      """)

    db.Close_db(cur, conn)
    return True
  
  def Historico_Vendas(self):# Retorna extratos do mais recente ao mais antigo
    conn = db.Init_db()
    cur = conn.cursor()

    cur.execute(f"""SELECT comida.nome, pedido.quantidade_item, pedido.data_pedido FROM comida 
    INNER JOIN pedido ON comida.codigo_comida=pedido.codigo_comida 
    WHERE comida.codigo_restaurante='{self.cnpj}' 
    ORDER BY pedido.data_pedido DESC;""")
    
    relatorio = cur.fetchall()
    if relatorio:
      print(f"""
      *******************\033[36m Relatório: Todas as vendas \033[37m *******************
      Comida\t\t\t \033[32m Quantidade\033[37m \t Data
      """)

      for item in relatorio:
        comida, quantidade, data = item
        print(f"\t{comida} \t \033[32m{quantidade}\033[37m \t {data}")
    else:
      print("\t\033[33m Não há nenhum cadastro de vendas! \033[37m\n")

    db.Close_db(cur, conn)
    return True

  def Media_Preco_Vendas(self):# Preço médio da comida vendida nos últimos 7 dias
    conn = db.Init_db()
    cur = conn.cursor()
    periodo = '1 months' 

    # Seleção do período
    opcao = input("""
    \033[36m[ 1 ]\033[37m - Obter relatório do último dia
    \033[36m[ 2 ]\033[37m - Obter relatório dos últimos 7 dias
    \033[36m[ 3 ]\033[37m - Obter relatório do mês
    -> """)

    if opcao == '1':
      periodo = '1 days'
    elif opcao == '2':
      periodo = '7 days'
    else: # Por default o restaurante verá o relatório do mẽs
      pass

    cur.execute(f"""SELECT AVG(preco_comida)::numeric(10,2),
    comida.nome FROM comida INNER JOIN item_pedido USING(codigo_comida) 
    INNER JOIN restaurante ON comida.codigo_restaurante='{self.cnpj}' 
    WHERE data_pedido > current_date - interval '{periodo}'
    GROUP BY comida.nome ;""")
    
    relatorio = cur.fetchall()
    if relatorio:
      print(f"""
      *******************\033[36m Relatório: Média do preço das vendidas no mês \033[37m *******************
      Comida\t\t\t \033[32m Preço(Médio)\033[37m
      """)

      for item in relatorio:
        media_preco, cod_comida = item
        print(f"\t{cod_comida} \t \033[32m{media_preco}\033[37m")
    else:
      print("\t\033[33m Não há nenhum cadastro de vendas! \033[37m\n")

    db.Close_db(cur, conn)
    return True