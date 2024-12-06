from models.aluno_model import usuario

class AlunoController:
    def __init__(self):
        self.model = usuario()

    def adicionar_usuario(self, nome, email, celular, aluno, professor):
        self.model.inserir(nome, email, celular, aluno, professor)

    def listar_usuarios(self):
        return self.model.buscar()

    def atualizar_usuario(self, nome, email, celular, aluno, professor, id):
        self.model.atualizar(nome, email, celular, aluno, professor, id)

    def deletar_usuario(self, id):
        self.model.deletar(id)

    def close(self):
        del self.model