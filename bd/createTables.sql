
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
  codigo_pedido INT PRIMARY KEY,
  data_pedido TIMESTAMP NOT NULL,
  total FLOAT NOT NULL,
  observacao TEXT,
  desconto FLOAT,
  finalizado BOOLEAN NOT NULL,
  codigo_cliente VARCHAR REFERENCES cliente(cpf)
);

CREATE TABLE item_pedido (
  preco_total FLOAT,
  quantidade INT,
  codigo_pedido  INT REFERENCES pedido(codigo_pedido),
  codigo_comida INT REFERENCES comida(codigo_comida),
  PRIMARY KEY (codigo_pedido),
  PRIMARY KEY (codigo_comida) 
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
VALUES ('33014556000199', 'Pizzaria do Paulista', 'paulista@gmail.com', '123456', 0.0, 'true');

INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99');

INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Pizza de doritos', 25.90, 'Doritos, queijo mussarela, molho de tomate', '33.014.556/0001-99');