-- Dados de teste --

-- Criando restaurantes
INSERT INTO restaurante (cnpj, nome, email, senha, entrega, aberto) 
VALUES ('33.014.556/0001-99', 'Pizzaria do Paulista', 'paulista@gmail.com', '123456', 0.0, 'true'),
('99.831.514/0001-56', 'HDO', 'hdo@gmail.com', 123, 'hdo', 0.0, 'True'),
('14.480.302/0001-19', 'Bar do Cuscuz', 'cuscuz@gmail.com', 'cuscuz', 0.0, 'true'),
('44.810.967/0001-04', 'Spoleto', 'spoleto@gmail.com', 'spoleto', 0.0, 'true'),
('17.526.380/0001-03', 'Panela de Barro', 'panela@gmail.com', 'panela', 0.0, 'true'),
('56.283.094/0001-08', 'Novo Oriente', 'oriente@gmail.com', 'oriente', 0.0, 'true'),
('11.175.890/0001-99', 'China Taiwan', 'china@gmail.com', 'china', 0.0, 'true')
;

-- Criando o cardápio de cada restaurante --

INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99')
;

-- Restaurante 2 --
INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99')
;

-- Restaurante 3 --
INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99')
;

-- Restaurante 4 --
INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99')
;

-- Restaurante 5 --
INSERT INTO comida (nome, preco, descricao, codigo_restaurante)
VALUES ('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99'),
('Hamburguer Especial', 35.60, 'Carne bovina, bacon, queijo do reino, tomate e cebola', '33.014.556/0001-99')
;

-- clientes --

INSERT INTO cliente (cpf, nome, email, senha, telefone1, telefone2)
VALUES ('956.531.015-08', 'Ana', 'ana@gmail.com', 'ana', '(81)1321655', '(81)1321655'),
('184.337.214-29', 'gustavo', 'gustavo@gmail.com', 'gustavo', '(81)1321655', '(81)1321655'),
('289.267.882-02', 'eraldo', 'eraldo@gmail.com', 'eraldo', '(81)1321655', '(81)1321655'),
('628.109.564-21', 'duda', 'duda@gmail.com', 'duda', '(81)1321655', '(81)1321655'),
('565.707.956-60', 'celia', 'celia@gmail.com', 'celia', '(81)1321655', '(81)1321655'),
('454.228.611-83', 'john', 'john@gmail.com', 'john', '(81)1321655', '(81)1321655');
