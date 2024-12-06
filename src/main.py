from controllers.aluno_controller import AlunoController
from views.aluno_view_esquerdo import AlunoViewEsquerdo
from views.aluno_view_direito import AlunoViewDireito
import customtkinter as ctk

def main():
    controller = AlunoController()
    root = ctk.CTk()

    view_esquerda = AlunoViewEsquerdo(root=root, controller=controller)
    view_direita = AlunoViewDireito(root=root, controller=controller)

    root.mainloop()

if __name__ == "__main__":
    main()