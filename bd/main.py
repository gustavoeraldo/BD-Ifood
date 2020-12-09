import psycopg2
import sys

from cliente import Cliente
from restaurante import Restaurante
from db import db

def Pesquisa_Usuario(tabela, email, senha):#Identifica o tipo do usuário e retorna seus dados
  conn = db.Init_db()
  cur = conn.cursor()
 
  try:
    cur.execute(f"SELECT * FROM {tabela} WHERE email='{email}' AND senha='{senha}';")
    user = cur.fetchone()
    print(f'Usuário : {user}')

    Menu(tabela, user)
    db.Close_db(cur, conn)
  except OSError as err:
    print(f'Usuário não existe, realize um cadastro!\n erro:{err} ')
  
  return  

def Login():

  tipo_usuario = input('Selecione o tipo de usuário \n'
  '(Digite 1 para pessoa física, 2 para pessoa jurídica ): ')

  email = input('Digite seu email:\n')
  senha = input('Digite sua senha:\n')

  conn = db.Init_db()
  cur = conn.cursor()

  if tipo_usuario == '1': 
   Pesquisa_Usuario('cliente', email, senha)

  elif tipo_usuario == '2':
    Pesquisa_Usuario('restaurante', email, senha)

  return 'Redireciona para o dashboard'

def Cadastro():# Cria Cliente ou restaurante
  tipo_usuario = input ('Você é um cliente ou dono de restaurante ? \n'
  '(Digite 1 para cliente ou 2 para restaurante)')

  if tipo_usuario == '1':
    cpf = input('Digite seu cpf: ')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite seu senha: ')
    telefone1 = input('Digite telefone principal: ')
    telefone2 = input('Digite telefone secundário: ')

    cliente1 = Cliente(cpf, nome, email, senha, telefone1, telefone2)
    return 'Cadastro realizado com sucesso'

  elif tipo_usuario == '2':
    cnpj = input('Digite seu cnpj: ')
    nome = input('Digite seu nome: ')
    entrega = input('Digite o valor da entrega: ')
    email = input('Digite seu email: ')
    senha = input('Digite seu senha: ')
    
    restaurante = Restaurante(cnpj, email, senha, nome, entrega, aberto)
    restaurante.Cadastrar()

    return 'é restaurante'

  else:
    print('Selecione uma das opções ou cancele a requisição')
    return 'Redireciona para o dashboard'

def Menu(tipo_usuario, info_usuario):
  loop = True

  while loop:
    print(f"\033[33m{'**'*9}\n"
      f"*\t Menu \t *\n"
      f"{'**'*9}\033[37m\n")

    if tipo_usuario == 'cliente':
      cpf, nome, email, senha, telefone1, _ = info_usuario
      cliente = Cliente(cpf, nome, email, senha, telefone1, _)

      opcao = input('\033[36m[ 1 ] - Atualizar perfil\n'
            '[ 2 ] - Buscar comida\n'
            '[ 3 ] - Buscar restaurante\n'
            '[ 4 ] - Visualizar todos os pedidos\n'
            '[ 5 ] - \033[31m Logout \033[37m\n')
      
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
      cnpj, email, senha, nome, entrega,aberto = info_usuario
      restaurante = Restaurante(cnpj, email, senha, nome, entrega,aberto)

      opcao = input('[ 1 ] - Atualizar cardápio\n'
            '[ 2 ] - Visualizar cardápio\n'
            '[ 3 ] - Obter relatório mensal\n'
            '[ 4 ] - \033[31m Logout \033[37m\n')
      
      if opcao == '1':
        loop = restaurante.Atualizar_Cardapio()
      elif opcao == '2':
        loop = restaurante.Visualizar_Cardapio()
      elif opcao == '3':
        loop = restaurante.Obter_relatorio()
      elif opcao == '4':
        loop = False

    print(loop)

  return 


print('Bem vindo ao iFood!')

if __name__ == '__main__':

  entrada = input(" Deseja fazer login ? (Digite 's' para sim. Caso não tenha login digite 'n'"
    'e realize um cadastro)')

  if entrada.lower() == 's':
    Login()
  elif entrada.lower() == 'n' :
    Cadastro()