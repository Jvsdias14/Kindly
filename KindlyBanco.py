CREATE TABLE instituicoes(id INT AUTO_INCREMENT PRIMARY KEY,      
nome VARCHAR(100),      
email VARCHAR(100),
codigo VARCHAR(100),
foto VARCHAR(100))  

CREATE TABLE doadores(id INT AUTO_INCREMENT PRIMARY KEY,      
nome VARCHAR(100),      
email VARCHAR(100),
senha VARCHAR(100),
foto VARCHAR(100));

CREATE TABLE cartoes(idcard INT AUTO_INCREMENT PRIMARY KEY,    
iduser VARCHAR(100),     
nomeuser VARCHAR(100),   
cpfuser VARCHAR(100),      
numcard VARCHAR(100), 
cvccard VARCHAR(100), 
vencicard VARCHAR(100),
bandeiracard VARCHAR(100));

insert into instituicoes (codigo) value ("gNojTsfagh");

''' 
a fazer:

- arrumar função clique entry
- Colocar * na senha
- Fazer botão de ver a senha
- Criar botão de logout
- Arrumar cadastro do cartão
- Criar post de exemplo

- Criar chat de exemplo
'''

CREATE TABLE postagem(id INT AUTO_INCREMENT PRIMARY KEY,      
idinst VARCHAR(100),      
mensagem VARCHAR(100),
foto VARCHAR(100)) 

CREATE TABLE instsrecentes(id INT AUTO_INCREMENT PRIMARY KEY,      
idinst VARCHAR(100),      
iddoador doador(100))

CREATE TABLE doacoesrecentes(id INT AUTO_INCREMENT PRIMARY KEY,      
idinst VARCHAR(100),      
valor VARCHAR(100),
iddoador VARCHAR(100))
