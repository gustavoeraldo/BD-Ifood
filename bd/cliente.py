# import psycopg2
import sys

from db import db

'''
restaurante:
[x] Bustar comida 
[ ] Buscar restaurante 
[ ] Histórico de pedidos
[ ] Alterar perfil
'''

class Cliente():
  def __init__(self, cpf, nome, email, senha, telefone1, telefone2):
    self.cpf = cpf
    self.nome = nome
    self.email =email
    self.senha = senha
    self.telefone1 = telefone1
    self.telefone2 = telefone2

  def Alterar_Perfil(self):
    return 'Perfil alterado com sucesso'

  def Buscar_Comida(self):
    conn = db.Init_db()
    cur = conn.cursor()
    '''
    [x] Continuar buscando comida
    [/] Selecionar uma comida e fazer o pedido
    [x] Cancela operação e volta para o Menu
    '''
    loop = True

    while loop:
      comida = input('Digite a comida que está procurando: ')

      if comida:
        cur.execute(f"""SELECT comida.nome, comida.preco, comida.codigo_comida, restaurante.nome FROM comida
        INNER JOIN restaurante ON comida.codigo_restaurante=restaurante.cnpj
        WHERE comida.nome ILIKE '{comida}%'""")
        
        resultado = cur.fetchall()

        if resultado:
          print("\t Comida \t\t Peço \t Restaurante\n")

          for item in resultado:
            nome, preco, _, restaurante = item
            print(f"\033[32m\t{nome}\033[37m \t R$ \033[33m {preco}\033[37m \t{restaurante} \n")

      opcao = input("""[ 1 ] - Continuar buscando comida
              [ 2 ] - Selecionar uma comida e fazer o pedido
              [ 3 ] - Voltar para o Menu\n""")

      if opcao == '1':
          pass
      elif opcao == '2':
        loop = self.Fazer_Pedido(conn, cur, resultado)
      elif opcao == '3':
        loop = False
      else: 
        pass

    db.Close_db(cur, conn)

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

  def Fazer_Pedido(self, cur, conn, lista_comida):
    conn = db.Init_db()
    cur = conn.cursor()
    i = 0

    for item in lista_comida:
      comida, preco, _, restaurante = item
      print(f"\033[32m\t[{i}]{comida}\033[37m \t R$ \033[33m {preco}\033[37m \t{restaurante} \n")
      i = i+1

    index = input('Selecione a comida que irá pedir: ')
    comida, preco, cod_comida, restaurante = lista_comida[int(index)]

    quantidade = input('Digite a quantidade desejada do item selecionado: ')
    observacao = input('Informe observações extra: ')

    total = int(quantidade)*preco
    
    print(f'Informação do pedido: {comida} \t {round(total, 2)} \t {restaurante}')

    confirmacao = input('Deseja confirmar o pedido ?: (S/N)')

    if confirmacao.lower() == 's':
      try:
        cur.execute(f"""INSERT INTO pedido(total, quantidade_item, observacao, finalizado, codigo_cliente, codigo_comida)
        VALUES ({round(total, 2)},{quantidade},'{observacao}',{'false'},'{self.cpf}','{cod_comida}')""")
        conn.commit()
      except OSError as err:
        print(err)
        return f'{err}'
    elif confirmacao.lower() == 'n':
      print('\n\033[31m Pedido Cancelado!\033[37m\n')
      return
    
    print('\n \033[32mPedido concluído com sucesso !\033[37m \n')

    return True