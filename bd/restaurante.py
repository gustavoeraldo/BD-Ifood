import psycopg2
import sys
import random

from db import db

'''
restaurante:
[x] crud de comida
[ ] relatório
  - comidas mais vendidas
  - extrato do mais recente ao mais antigo
  - preço médio da comida vendida nos últimos 7 dias
'''

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
    except OSError as err:
      return f'Erro no cadastro do restaurante. {err}' 
    
    db.Close_db(cur, conn)
    return True

  def Atualizar_Cardapio(self):

    loop = True

    while loop:
      opcao = input('[ 1 ] - Adicionar comida\n'
              '[ 2 ] - Editar comida\n'
              '[ 3 ] - Deletar comida\n'
              '[ 4 ] - Cancelar operação\n')

      if opcao == '1':
          loop = self.Adicionar_Comida()
      elif opcao == '2':
        loop = self.Editar_Comida()
      elif opcao == '3':
        loop = self.Deletar_Comida()
      elif opcao == '4':
          loop = False
      
      print(loop)

    return True

  def Adicionar_Comida(self):

    conn = db.Init_db()
    cur = conn.cursor()
    
    nome = input('Digite o nome da comida (máximo de 25 caracteres):\n') 
    preco = input('Digite o preco da comida:\n') 
    descricao = input('Digite o descrição da comida (máximo de 100 caracteres):\n')  

    try:
      cur.execute(f"INSERT INTO comida VALUES {random.randrange(6, 10**5), nome, float(preco), descricao, self.cnpj};")
      conn.commit()
    except OSError as err:
      print(f'Erro: {err}')
      return f'{err}'
    
    db.Close_db(cur, conn)

    return 'Comida adicionada com sucesso!'
    
  def Deletar_Comida(self):
    conn = db.Init_db()
    cur = conn.cursor()

    self.Visualizar_Cardapio()
    comida = input('Digite a comida que deseja deletar:\n')
   
    try:
      cur.execute(f"DELETE FROM comida WHERE nome='{comida}' AND codigo_restaurante='{self.cnpj}'")  
      conn.commit()
    except OSError as err:
      print(err)
      return f'{err}'
    
    db.Close_db(cur, conn)
    return True

  def Editar_Comida(self):
    conn = db.Init_db()
    cur = conn.cursor()

    self.Visualizar_Cardapio()
    antiga_comida = input('Digite o nome da comida que deseja alterar:\n')
    novo_nome = input('Digite o novo nome da comida:\n')

    try:
      cur.execute(f"UPDATE comida SET nome='{novo_nome}' WHERE nome='{antiga_comida}' AND codigo_restaurante='{self.cnpj}'")  
      conn.commit()
    except OSError as err:
      print(err)
      return f'{err}'
    
    db.Close_db(cur, conn)
    return 'retorna uma ou várias comidas'

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

  def Obter_relatorio(self):
    print('Relatório do mês')
    return True