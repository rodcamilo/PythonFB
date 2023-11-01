--https://sqliteonline.com/
--criação de banco de dados
--CREATE DATABASE SaoPauloFC;

--conexão com banco de dados
--USE SaoPauloFC;

--criação de tabela
CREATE TABLE Jogadores (
ID INT PRIMARY KEY,
Nome VARCHAR(50),
Posicao VARCHAR(50),
Salario DECIMAL(10,2)
);

--inserção de dados
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (1, 'Rafael', 'Goleiro', 150000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (2, 'Rafinha', 'Lateral', 200000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (3, 'Beraldo', 'Zagueiro', 200000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (4, 'Arboleda', 'Zagueiro', 250000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (6, 'Caio Paulista', 'Lateral', 150000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (5, 'Pablo Maia', 'Volante', 150000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (8, 'Rodrigo Nestor', 'Volante', 150000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (7, 'Lucas', 'Atacante', 350000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (9, 'Calleri', 'Atacante', 300000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (10, 'James Rodrigues', 'Meia', 350000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (11, 'Luciano', 'Atacante', 250000.00);
INSERT INTO Jogadores (ID, Nome, Posicao, Salario)
VALUES (12, 'Alison', 'Volante', 150000.00);

--seleção de dados
SELECT * FROM Jogadores
ORDER BY Salario DESC;

--atualização de dados
UPDATE Jogadores
SET Salario = 350000.00
WHERE ID = 9;

--deletar banco de dados
DELETE FROM Jogadores
WHERE ID = 12;