import psycopg2
import sys

from db import db

class Cliente():
  def __init__(self, cpf, nome, email, senha, telefone1, telefone2):
    self.cpf = cpf
    self.nome = nome
    self.email =email
    self.senha = senha
    self.telefone1 = telefone1
    self.telefone2 = telefone2

  def Alterar_perfil(self):
    return 'Perfil alterado com sucesso'

  def Buscar_Comida(self):
    return 'lista de comidas'

  def Buscar_Restaurante(self):
    return 'buscar restaurante'

  def Cadastrar(self):
    conn = db.Init_db()
    cur = conn.cursor()

    try:
      cur.execute(f"INSERT INTO cliente VALUES ({cpf, nome, email, senha, telefone1});")
      conn.commit()
    except OSError as err:
      return f'Erro na criação do restaurante. {err}' 
    
    print('Usuário cadastrado com sucesso!')

    db.Close(cur, conn)
    return True

  def Fazer_Pedido(self):
    return 'pedido concluído com sucesso !'