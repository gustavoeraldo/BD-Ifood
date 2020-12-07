import psycopg2

'''
cliente: 
- buscar comida
- buscar restaurante
- fazer pedido

'''

class Cliente():
  def __init__(self, cpf, nome, email, senha, telefone1, telefone2):
    self.cpf = cpf
    self.nome = nome
    self.email =email
    self.senha = senha
    self.telefone1 = telefone1
    self.telefone2 = telefone2

    conn = psycopg2.connect(dbname="ifood", user="postgres", password="docker", host="localhost", port=5435)
    cur = conn.cursor()

    cur.execute(f"INSERT INTO cliente (cpf, nome, email, senha, telefone1) VALUES {cpf, nome, email, senha, telefone1};")
    conn.commit()

    cur.close()
    conn.close()

    print(f'Criando usuário {nome}')

  def buscar_comida(self):
    return 'lista de comidas'

  def buscar_restaurante(self):
    return 'buscar restaurante'

  def fazer_pedido(self):
    return 'pedido concluído com sucesso !'