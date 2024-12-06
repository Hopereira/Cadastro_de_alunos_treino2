# Sistema de Gerenciamento de Usuários

Este projeto é um sistema simples de gerenciamento de usuários em Python, utilizando SQLite para armazenamento de dados e `customtkinter` para a interface gráfica.

## Estrutura do Projeto

- `doc/`: Documentação do projeto.
- `test/`: Testes unitários e de integração.
- `src/`: Código-fonte do projeto.
  - `controllers/`: Controladores que lidam com a lógica de entrada e saída.
  - `models/`: Modelos que representam a lógica de dados e interagem com o banco de dados.
  - `views/`: Views que apresentam os dados ao usuário.
    - `aluno_view_esquerdo.py`: Frame esquerdo para entrada de dados e manipulação.
    - `aluno_view_direito.py`: Frame direito para busca e resultado.
  - `main.py`: Arquivo principal que inicializa o aplicativo.
- `db/`: Arquivos relacionados ao banco de dados.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Visão geral do projeto, instruções de instalação e uso.

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
Crie um ambiente virtual e ative-o:

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instale as dependências:

pip install -r requirements.txt
Uso
Execute o aplicativo:

python src/main.py
Use a interface gráfica para adicionar, atualizar, deletar e buscar usuários.

Estrutura do Banco de Dados
O banco de dados SQLite é armazenado na pasta db e contém uma tabela usuario com os seguintes campos:

id: Identificador único do usuário (INTEGER, PRIMARY KEY, AUTOINCREMENT)
nome: Nome do usuário (TEXT, NOT NULL)
email: E-mail do usuário (TEXT, NOT NULL)
celular: Celular do usuário (TEXT, NOT NULL)
aluno: Indica se o usuário é aluno (BOOLEAN, NOT NULL)
professor: Indica se o usuário é professor (BOOLEAN, NOT NULL)
Contribuição
Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/nova-feature).
Commit suas mudanças (git commit -am 'Adiciona nova feature').
Faça push para a branch (git push origin feature/nova-feature).
Crie um novo Pull Request.
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.


Este `README.md` fornece uma visão geral clara do projeto, instruções de instalação e uso, e detalhes sobre a estrutura do projeto e do banco de dados. Se precisar de mais alguma coisa ou tiver outras dúvidas, estou aqui para ajudar!