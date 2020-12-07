import psycopg2

from cliente import Cliente
from restaurante import Restaurante
from db import db

def Login():

  email = input('Digite seu email:\n')
  senha = input('Digite sua senha:\n')

  conn = db.Init_db()
  cur = conn.cursor()

  try:
    cur.execute('SELECT email, senha FROM cliente WHERE email=%s AND senha=%s;', (email, senha))
    user = cur.fetchone()
    print(f'Usuário : {user}')
  except:
    print('Usuário não existe, realize um cadastro! ') 

  return 'Redireciona para o dashboard'

  db.Close_db(cur, conn)

def Cadastro():# Cria Cliente ou restaurante
  tipo_usuario = input ('Você é um cliente ou dono de restaurante ? \n'
  '(Digite 1 para cliente ou 2 para restaurante)')

  if tipo_usuario == '1':
    cpf = input('Digite seu cpf')
    nome = input('Digite seu nome')
    email = input('Digite seu email')
    senha = input('Digite seu senha')
    telefone1 = input('Digite seu telefone')
    telefone2 = input('Digite segundo telefone')

    cliente1 = Cliente(cpf, nome, email, senha, telefone1, telefone2)

    return 'Cadastro realizado com sucesso'
  else:
    return 'é restaurante'

  return 'Redireciona para o dashboard'

def Menu():
  return 'aqui é o menu'


print('Bem vindo ao iFood!')

'''
voce já possui uma conta ?
sim: goto (login)
não: faz um cadastro 

Login():
caso cliente 
  cliente dashboard
caso restaurante 
  restaurante dashboard

Cadasto():
  - escolher o tipo do usuário
  - preencher os dados
  - redirecionar para o dashboard
'''

entrada = input('Deseja fazer login ? (Caso não tenha login digite não'
  'e realize um cadastro)')

if entrada == 'sim':
  Login()
else:
  Cadastro()
