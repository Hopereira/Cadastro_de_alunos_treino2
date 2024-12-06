#importando bibliotecas necessárias
import sqlite3
import os

#criado a classe usuario
class usuario:
    #criando a conexão com o banco de dados
    def __init__(self):
       try:
           # Certifique-se de que a pasta db existe
           if not os.path.exists('db'):
               os.makedirs('db')
           self.connection = sqlite3.connect('db/database.db')
           print('Conexão com o banco de dados estabelecida')
           self.cursor = self.connection.cursor()
           self.criar_tabela()
       except sqlite3.Error as e:
           print(f'Erro ao conectar ao banco de dados: {e}')

    def criar_tabela(self):
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                celular TEXT NOT NULL,
                aluno BOOLEAN NOT NULL,
                professor BOOLEAN NOT NULL
            )
            ''')
            self.connection.commit()
            print('Tabela criada com sucesso')  
        except sqlite3.Error as e:
            print(f'Erro ao criar tabela: {e}')

    def inserir(self, nome, email, celular, aluno, professor):
        try:
            self.cursor.execute('''
            INSERT INTO usuario(nome, email, celular, aluno, professor)
            VALUES(?,?,?,?,?)
            ''', (nome, email, celular, aluno, professor))
            self.connection.commit()
            print('Usuário inserido com sucesso')
        except sqlite3.Error as e:
            print(f'Erro ao inserir usuário: {e}')

    def buscar(self):
        try:
            self.cursor.execute('SELECT * FROM usuario')
            usuarios = self.cursor.fetchall()
            return usuarios
        except sqlite3.Error as e:
            print(f'Erro ao buscar usuários: {e}')
            return []
    
    def atualizar(self, nome, email, celular, aluno, professor, id):
        try:
            self.cursor.execute('''
            UPDATE usuario SET nome=?, email=?, celular=?, aluno=?, professor=? WHERE id=?
            ''', (nome, email, celular, aluno, professor, id))
            self.connection.commit()
            print('Usuário atualizado com sucesso')
        except sqlite3.Error as e:
            print(f'Erro ao atualizar usuário: {e}')

    def deletar(self, id):
        try:
            self.cursor.execute('''
            DELETE FROM usuario WHERE id=?
            ''', (id,))
            self.connection.commit()
            print('Usuário deletado com sucesso')
        except sqlite3.Error as e:
            print(f'Erro ao deletar usuário: {e}')

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print('Conexão com o banco de dados encerrada')