import psycopg2
import sys

from cliente import Cliente
from restaurante import Restaurante
from db import db

def Pesquisa_Usuario(tabela, email, senha):#Identifica o tipo do usuário e retorna seus dados
  conn = db.Init_db()
  cur = conn.cursor()

  cur.execute(f"SELECT * FROM {tabela} WHERE email='{email}' AND senha='{senha}';")
  user = cur.fetchone()
  db.Close_db(cur, conn)

  if user:
    Menu(tabela, user)
  else:
    print('\033[31m\tUsuário não existe ou os dados estão incorretos!\033[37m\n')
  return
  
  
  return  

def Login():
  conn = db.Init_db()
  cur = conn.cursor()
  print('\n\033[32m\t ************* Faça o Login no sistema *************\033[37m\n')

  tipo_usuario = input('Selecione o tipo de usuário \n'
  '(Digite 1 para pessoa física, 2 para pessoa jurídica ): ')

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
  
  tipo_usuario = input ('''
  Você é um cliente ou dono de restaurante ?
  (Digite 1 para cliente ou 2 para restaurante): ''')

  if tipo_usuario == '1':
    cpf = input('\nDigite seu cpf: ')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite seu senha: ')
    telefone1 = input('Digite telefone principal: ')
    telefone2 = input('Digite telefone secundário: ')

    cliente = Cliente(cpf, nome, email, senha, telefone1, telefone2)
    cadastro_req = cliente.Cadastrar()# Efetua o cadastro

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
    restaurante.Cadastrar()

    return 'é restaurante'

  else:
    print('Selecione uma das opções ou cancele a requisição')
    return 'Redireciona para o dashboard'

def Menu(tipo_usuario, info_usuario):
  print('\t\nLogin efetuado\n')
  loop = True

  while loop:
    print(f"""
      \033[33m{'**'*8}
      *\t Menu do app *
      {'**'*8}\033[37m\n""")

    if tipo_usuario == 'cliente':
      cpf, nome, email, senha, telefone1, _ = info_usuario
      cliente = Cliente(cpf, nome, email, senha, telefone1, _)

      opcao = input("""
      \033[36m[ 1 ]\033[37m - Atualizar perfil
      \033[36m[ 2 ]\033[37m - Buscar comida
      \033[36m[ 3 ]\033[37m - Buscar restaurante
      \033[36m[ 4 ]\033[37m - Visualizar todos os pedidos
      \033[36m[ 5 ] -\033[31m Logout \033[37m
      -> """)
      
      if opcao == '1':
        loop = cliente.Alterar_Perfil()
      elif opcao == '2':
        loop = cliente.Buscar_Comida()
      elif opcao == '3':
        loop = cliente.Buscar_Restaurante()
      elif opcao == '4':
        loop = cliente.Visualizar_Historico()
      elif opcao == '5':
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


print('Bem vindo ao NewiFood!')

if __name__ == '__main__':

  entrada = input('''
    Deseja fazer login ? (Digite \033[32m's' para sim\033[37m.
    Caso\033[33m não tenha login digite 'n'\033[37m\033[36m e realize um cadastro\033[37m: )''')

  if entrada.lower() == 's':
    Login()
  elif entrada.lower() == 'n' :
    Cadastro()