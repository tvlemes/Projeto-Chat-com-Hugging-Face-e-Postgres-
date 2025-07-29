-- Definição do encoding
SET client_encoding = 'UTF8';

-- Remover tabelas anteriores, se existirem
DROP TABLE IF EXISTS vendas, produtos, clientes CASCADE;

-- Criar tabela de produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2)
);

-- Inserir 20 produtos
INSERT INTO produtos (nome, preco) VALUES
('Notebook', 3500.00),
('Mouse', 60.00),
('Teclado', 150.00),
('Monitor', 1200.00),
('Impressora', 700.00),
('Webcam', 200.00),
('Fone de ouvido', 100.00),
('HD Externo', 250.00),
('Pendrive 32GB', 30.00),
('Pendrive 64GB', 50.00),
('SSD 512GB', 400.00),
('SSD 1TB', 700.00),
('Gabinete Gamer', 300.00),
('Placa-mãe', 1000.00),
('Placa de vídeo', 2500.00),
('Fonte 600W', 350.00),
('Cadeira gamer', 1200.00),
('Cooler', 80.00),
('Mousepad', 25.00),
('Notebook Gamer', 6000.00);

-- Criar tabela de clientes
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

-- Inserir 30 clientes
INSERT INTO clientes (nome, email) VALUES
('Ana Silva', 'ana@gmail.com'),
('Bruno Souza', 'bruno@gmail.com'),
('Carlos Lima', 'carlos@gmail.com'),
('Daniela Rocha', 'daniela@gmail.com'),
('Eduardo Nunes', 'eduardo@gmail.com'),
('Fernanda Costa', 'fernanda@gmail.com'),
('Gabriel Alves', 'gabriel@gmail.com'),
('Helena Castro', 'helena@gmail.com'),
('Igor Pereira', 'igor@gmail.com'),
('Joana Martins', 'joana@gmail.com'),
('Kleber Oliveira', 'kleber@gmail.com'),
('Larissa Dias', 'larissa@gmail.com'),
('Marcos Teixeira', 'marcos@gmail.com'),
('Nathalia Melo', 'nathalia@gmail.com'),
('Otavio Braga', 'otavio@gmail.com'),
('Paula Vieira', 'paula@gmail.com'),
('Rafael Cunha', 'rafael@gmail.com'),
('Simone Rios', 'simone@gmail.com'),
('Thiago Lemes', 'thiago@gmail.com'),
('Ursula Matos', 'ursula@gmail.com'),
('Vinicius Torres', 'vinicius@gmail.com'),
('Wesley Lopes', 'wesley@gmail.com'),
('Xuxa Meneghel', 'xuxa@gmail.com'),
('Yasmin Santos', 'yasmin@gmail.com'),
('Zeca Pagodinho', 'zeca@gmail.com'),
('Bruna Lima', 'bruna@gmail.com'),
('Cesar Monteiro', 'cesar@gmail.com'),
('Davi Ramos', 'davi@gmail.com'),
('Elaine Farias', 'elaine@gmail.com'),
('Fabiana Luz', 'fabiana@gmail.com');

-- Criar tabela de vendas
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    produto_id INT REFERENCES produtos(id),
    quantidade INT,
    data DATE
);

-- Inserir 15 vendas
INSERT INTO vendas (cliente_id, produto_id, quantidade, data) VALUES
(1, 1, 1, '2025-07-01'),
(2, 2, 2, '2025-07-02'),
(3, 3, 1, '2025-07-03'),
(4, 4, 1, '2025-07-04'),
(5, 5, 3, '2025-07-05'),
(6, 6, 1, '2025-07-06'),
(7, 7, 2, '2025-07-07'),
(8, 8, 1, '2025-07-08'),
(9, 9, 4, '2025-07-09'),
(10, 10, 2, '2025-07-10'),
(11, 11, 1, '2025-07-11'),
(12, 12, 1, '2025-07-12'),
(13, 13, 2, '2025-07-13'),
(14, 14, 1, '2025-07-14'),
(15, 15, 1, '2025-07-15');
