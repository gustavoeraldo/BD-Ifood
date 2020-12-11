
-- Tabelas relacionadas ao cliente --

CREATE TABLE cliente (
  cpf VARCHAR PRIMARY KEY,
  nome VARCHAR NOT NULL,
  email VARCHAR NOT NULL,
  senha VARCHAR NOT NULL,
  telefone1 VARCHAR,
  telefone2 VARCHAR
);

CREATE TABLE endereco (
  codigo_endereco INT PRIMARY KEY,
  rua VARCHAR NOT NULL,
  bairro VARCHAR NOT NULL,
  numero INT NOT NULL,
  codigo_cliente VARCHAR REFERENCES cliente(cpf)
);

-- Pedidos --
CREATE TABLE pedido (
  codigo_pedido SERIAL PRIMARY KEY,
  data_pedido TIMESTAMP DEFAULT NOW () NOT NULL,
  total FLOAT NOT NULL,
  quantidade_item INT NOT NULL,
  observacao TEXT,
  finalizado BOOLEAN NOT NULL,
  codigo_cliente VARCHAR REFERENCES cliente(cpf) NOT NULL,
  codigo_comida INT REFERENCES comida(codigo_comida) NOT NULL
);

CREATE TABLE item_pedido (
  preco_comida FLOAT NOT NULL,
  data_pedido TIMESTAMP DEFAULT NOW () NOT NULL,
  codigo_pedido INT REFERENCES pedido(codigo_pedido) NOT NULL,
  codigo_comida INT REFERENCES comida(codigo_comida) NOT NULL
);

CREATE TABLE comida (
  codigo_comida SERIAL PRIMARY KEY,
  nome VARCHAR(25) NOT NULL,
  preco FLOAT NOT NULL,
  descricao VARCHAR(100),
  codigo_restaurante VARCHAR REFERENCES restaurante(cnpj) NOT NULL
);

-- Tabelas associadas ao usuário restaurante --

CREATE TABLE restaurante (
  cnpj VARCHAR(14) PRIMARY KEY,
  nome VARCHAR(30) NOT NULL,
  email VARCHAR(30) NOT NULL,
  senha VARCHAR(30) NOT NULL,
  entrega FLOAT,
  aberto BOOLEAN NOT NULL
);

CREATE TABLE categoria (
  codigo_restaurante VARCHAR REFERENCES restaurante(cnpj),
  nome VARCHAR NOT NULL,
  PRIMARY KEY (codigo_restaurante)
);


-- Inserir fake dados nas tabelas --

INSERT INTO restaurante (cnpj, nome, email, senha, entrega, aberto) 
VALUES ('33.014.556/0001-99', 'Pizzaria do Paulista', 'paulista@gmail.com', '123456', 0.0, 'true');

INSERT INTO restaurante(cnpj, email, senha, nome, entrega, aberto) 
VALUES ('33.014.556/0001-96', 'rest@gmail.com', 123, 'Insano', 0.0, 'True')

INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99');

INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Pizza de doritos', 25.90, 'Doritos, queijo mussarela, molho de tomate', '33.014.556/0001-99');

-- Pesquisa de comida -- 
SELECT comida.nome, comida.preco, restaurante.nome FROM comida 
INNER JOIN restaurante ON comida.codigo_restaurante=restaurante.cnpj
WHERE comida.nome ILIKE 'ham%'

SELECT AVG(DISTINCT preco_comida)::numeric(10,2) FROM item_pedido 
INNER JOIN comida USING(codigo_comida) 
INNER JOIN restaurante ON comida.codigo_restaurante='33.014.556/0001-99' 
GROUP BY codigo_comida

SELECT AVG(DISTINCT preco_comida)::numeric(10,2),codigo_comida 
FROM item_pedido INNER JOIN comida USING(codigo_comida) 
INNER JOIN restaurante ON comida.codigo_restaurante='33.014.556/3124-11' 
GROUP BY codigo_comida