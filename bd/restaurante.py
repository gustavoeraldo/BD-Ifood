import psycopg2

'''
restaurante:
- crud de comida
- relatório
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
  
  def adicionar_comida(self):
    return 'retorna uma ou várias comidas'
    
  def deletar_comida(self):
    return 'retorna uma ou várias comidas'

  def editar_comida(self,comida_id):
    return 'retorna uma ou várias comidas'

  def ler_comida(self):
    return 'retorna uma ou várias comidas'

  def obter_relatorio(self):
    return 'relatório do mês'