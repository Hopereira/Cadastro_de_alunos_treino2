import customtkinter as ctk
import tkinter as tk

class AlunoViewDireito:
    def __init__(self, root, controller):
        self.controller = controller
        self.frame_direito = ctk.CTkFrame(master=root)
        self.frame_direito.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.label_resultado = ctk.CTkLabel(master=self.frame_direito, text="Busca e Resultado", font=("Arial", 24))
        self.label_resultado.pack(pady=12, padx=10)

        # Campo de busca perto do botão buscar
        self.search_id_entry = ctk.CTkEntry(master=self.frame_direito, placeholder_text="ID para buscar")
        self.search_id_entry.pack(pady=12, padx=10)

        self.search_button = ctk.CTkButton(master=self.frame_direito, text="Buscar Usuário", command=self.buscar_usuario)
        self.search_button.pack(pady=12, padx=10)

        self.list_button = ctk.CTkButton(master=self.frame_direito, text="Listar Usuários", command=self.listar_usuarios)
        self.list_button.pack(pady=12, padx=10)

        self.text_area = ctk.CTkTextbox(master=self.frame_direito, width=400, height=400)
        self.text_area.pack(pady=12, padx=10)

    def listar_usuarios(self):
        try:
            usuarios = self.controller.listar_usuarios()
            self.text_area.delete(1.0, tk.END)
            if usuarios:
                for usuario in usuarios:
                    self.text_area.insert(tk.END, f"{usuario}\n")
            else:
                self.text_area.insert(tk.END, "Nenhum usuário encontrado.\n")
        except Exception as e:
            self.text_area.insert(tk.END, f"Erro ao listar usuários: {e}\n")

    def buscar_usuario(self):
        try:
            id_str = self.search_id_entry.get()
            if id_str.isdigit():
                id = int(id_str)
                usuarios = self.controller.listar_usuarios()
                self.text_area.delete(1.0, tk.END)
                usuario_encontrado = False
                for usuario in usuarios:
                    if usuario[0] == id:
                        self.text_area.insert(tk.END, f"{usuario}\n")
                        usuario_encontrado = True
                        break
                if not usuario_encontrado:
                    self.text_area.insert(tk.END, "Usuário não encontrado.\n")
            else:
                self.text_area.insert(tk.END, "ID inválido.\n")
        except Exception as e:
            self.text_area.insert(tk.END, f"Erro ao buscar usuário: {e}\n")