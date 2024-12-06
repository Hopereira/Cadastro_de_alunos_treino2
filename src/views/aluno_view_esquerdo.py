import customtkinter as ctk
import tkinter as tk
from controllers.aluno_controller import AlunoController

class AlunoViewEsquerdo:
    def __init__(self, root, controller):
        self.controller = controller
        self.frame_esquerdo = ctk.CTkFrame(master=root)
        self.frame_esquerdo.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.label = ctk.CTkLabel(master=self.frame_esquerdo, text="Entrada de Dados", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)

        self.nome_entry = ctk.CTkEntry(master=self.frame_esquerdo, placeholder_text="Nome")
        self.nome_entry.pack(pady=12, padx=10)

        self.email_entry = ctk.CTkEntry(master=self.frame_esquerdo, placeholder_text="E-mail")
        self.email_entry.pack(pady=12, padx=10)

        self.celular_entry = ctk.CTkEntry(master=self.frame_esquerdo, placeholder_text="Celular")
        self.celular_entry.pack(pady=12, padx=10)

        self.aluno_var = tk.BooleanVar()
        self.aluno_check = ctk.CTkCheckBox(master=self.frame_esquerdo, text="Aluno", variable=self.aluno_var)
        self.aluno_check.pack(pady=12, padx=10)

        self.professor_var = tk.BooleanVar()
        self.professor_check = ctk.CTkCheckBox(master=self.frame_esquerdo, text="Professor", variable=self.professor_var)
        self.professor_check.pack(pady=12, padx=10)

        self.id_entry = ctk.CTkEntry(master=self.frame_esquerdo, placeholder_text="ID (para atualizar/deletar)")
        self.id_entry.pack(pady=12, padx=10)

        self.add_button = ctk.CTkButton(master=self.frame_esquerdo, text="Adicionar Usuário", command=self.adicionar_usuario)
        self.add_button.pack(pady=12, padx=10)

        self.update_button = ctk.CTkButton(master=self.frame_esquerdo, text="Atualizar Usuário", command=self.atualizar_usuario)
        self.update_button.pack(pady=12, padx=10)

        self.delete_button = ctk.CTkButton(master=self.frame_esquerdo, text="Deletar Usuário", command=self.deletar_usuario)
        self.delete_button.pack(pady=12, padx=10)

    def adicionar_usuario(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        celular = self.celular_entry.get()
        aluno = self.aluno_var.get()
        professor = self.professor_var.get()
        self.controller.adicionar_usuario(nome, email, celular, aluno, professor)

    def atualizar_usuario(self):
        try:
            id_str = self.id_entry.get()
            if id_str.isdigit():
                id = int(id_str)
                nome = self.nome_entry.get()
                email = self.email_entry.get()
                celular = self.celular_entry.get()
                aluno = self.aluno_var.get()
                professor = self.professor_var.get()
                self.controller.atualizar_usuario(nome, email, celular, aluno, professor, id)
            else:
                print("ID inválido.")
        except ValueError as e:
            print(f"Erro ao atualizar usuário: {e}")

    def deletar_usuario(self):
        try:
            id_str = self.id_entry.get()
            if id_str.isdigit():
                id = int(id_str)
                self.controller.deletar_usuario(id)
            else:
                print("ID inválido.")
        except ValueError as e:
            print(f"Erro ao deletar usuário: {e}")