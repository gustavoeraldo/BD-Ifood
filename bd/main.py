import sys

from cliente import Cliente
from restaurante import Restaurante
from db import db

def Pesquisa_Usuario(tabela, email, senha):#Identifica o tipo do usuário e retorna seus dados
  conn = db.Init_db()
  cur = conn.cursor()
  resposta = ''

  cur.execute(f"SELECT * FROM {tabela} WHERE email='{email}' AND senha='{senha}';")
  user = cur.fetchone()
  db.Close_db(cur, conn)

  if user:
    Menu(tabela, user)
  else:
    resposta = input(f"""\033[31m 
    Usuário não existe ou os dados estão incorretos!\033[37m
    Você deseja redirecionado para o Login novamente ?
    (S/N) -> """)
  
  if resposta.lower() == 's':
    Login()
  elif resposta.lower() == 'n': # Tratar essa opção
    print('Você saiu do app, Volte sempre!')
    return

  return  

def Login():
  conn = db.Init_db()
  cur = conn.cursor()
  print('\n\033[32m\t ************* Faça o Login no sistema *************\033[37m\n')

  tipo_usuario = input("""Selecione o tipo de usuário:
  [ 1 ] - Login de cliente 
  [ 2 ] - Login Restaurante
  -> """)

  if tipo_usuario == '1': 
    email = input('\nDigite seu email: ')
    senha = input('Digite sua senha: ')
    Pesquisa_Usuario('cliente', email, senha)

  elif tipo_usuario == '2':
    email = input('\nDigite seu email: ')
    senha = input('Digite sua senha: ')
    Pesquisa_Usuario('restaurante', email, senha)

  return True

def Cadastro():# Cria Cliente ou restaurante
  print('\n\033[32m\t ************* Cadastro no sistema *************\033[37m\n')
  resposta = ''
  cadastro_req = []

  tipo_usuario = input ('''
  Selecione o tipo do usuário: 
  [ 1 ] - cliente
  [ 2 ] - restaurante
  -> ''')

  if tipo_usuario == '1':
    cpf = input('\nDigite seu cpf: ')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite seu senha: ')
    telefone1 = input('Digite telefone principal: ')
    telefone2 = input('Digite telefone secundário (opcional): ')

    cliente = Cliente(cpf, nome, email, senha, telefone1, telefone2)
    try:
      cadastro_req = cliente.Cadastrar()# Efetua o cadastro
    except Exception as e:#e.__class__
      resposta = input('''Ocorreu erro no cadastro, revise suas informações.
      Você deseja redirecionado para o cadastro novamente ?
      (S/N) -> ''')
    
    if resposta.lower() == 's':
      Cadastro()
    elif resposta.lower() == 'n': # Tratar essa opção
      return

    if cadastro_req:# Em caso de sucesso no cadastro, redireciona para o login
      Login()

    return

  elif tipo_usuario == '2':
    cnpj = input('Digite seu cnpj: ')
    nome = input('Digite seu nome: ')
    entrega = input('Digite o valor da entrega: ')
    email = input('Digite seu email: ')
    senha = input('Digite seu senha: ')
    
    restaurante = Restaurante(cnpj, email, senha, nome, entrega, True)
    try:
      cadastro_req = restaurante.Cadastrar()
    except Exception as e:
      resposta = input('''Ocorreu erro no cadastro, revise suas informações.
      Você deseja redirecionado para o cadastro novamente ?
      (S/N) -> ''')

    if resposta.lower() == 's':
      Cadastro()
    elif resposta.lower() == 'n': # Tratar essa opção
      return

    if cadastro_req:# Em caso de sucesso no cadastro, redireciona para o login
      Login()

  return

def Menu(tipo_usuario, info_usuario):
  print('\t\nLogin efetuado\n')
  loop = True

  while loop:
    print("\033[33m **************** MENU DO APP ************** \033[37m")

    if tipo_usuario == 'cliente':
      cpf, nome, email, senha, telefone1, _ = info_usuario
      cliente = Cliente(cpf, nome, email, senha, telefone1, _)

      opcao = input("""
      \033[36m[ 1 ]\033[37m - Buscar comida
      \033[36m[ 2 ]\033[37m - Buscar restaurante
      \033[36m[ 3 ]\033[37m - Visualizar todos os pedidos
      \033[36m[ 4 ] -\033[31m Logout \033[37m
      -> """)
      
      if opcao == '1':
        loop = cliente.Buscar_Comida()
      elif opcao == '2':
        loop = cliente.Buscar_Restaurante()
      elif opcao == '3':
        loop = cliente.Visualizar_Historico()
      elif opcao == '4':
        loop = False

    elif tipo_usuario == 'restaurante':
      cnpj, email, senha, nome, entrega, aberto = info_usuario
      restaurante = Restaurante(cnpj, email, senha, nome, entrega, aberto)

      opcao = input("""
      \033[36m[ 1 ]\033[37m - Atualizar cardápio
      \033[36m[ 2 ]\033[37m - Visualizar cardápio
      \033[36m[ 3 ]\033[37m - Obter relatório de vendas
      \033[36m[ 4 ] -\033[31m Logout \033[37m
      -> """)
      
      if opcao == '1':
        loop = restaurante.Atualizar_Cardapio()
      elif opcao == '2':
        loop = restaurante.Visualizar_Cardapio()
      elif opcao == '3':
        loop = restaurante.Obter_relatorio()
      elif opcao == '4':
        loop = False

  print('''
    Volte sempre !
  ''')
  return 


if __name__ == '__main__':
  print('Bem vindo ao NewiFood!')

  entrada = input('''
  Deseja fazer login ? 
  \033[36m[ 1 ]\033[37m - Realizar Login
  \033[36m[ 2 ]\033[37m - Realizar Cadastro
  \033[36m[ 3 ]\033[37m - Sair do app
  ''')

  if entrada == '1':
    Login()
  elif entrada == '2' :
    Cadastro()
  elif entrada == '3':
    print('Volte sempre!')