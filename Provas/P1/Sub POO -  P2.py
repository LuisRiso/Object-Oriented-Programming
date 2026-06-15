# sub poo - p2

import tkinter as tk
from tkinter import messagebox, ttk

# definir a classe Professor p/ guardar as informações dos professores
class Professor:
    # construtor da classe Professor
    def __init__(self, cpf, nome, email, valor_pilates, valor_funcional):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.valor_pilates = valor_pilates
        self.valor_funcional = valor_funcional

    # property p/ obter o valor do pilates
    @property
    def valor_pilates(self):
        return self._valor_pilates

    # setter p/ definir que o valor do pilates seja apenas um valor positivo
    @valor_pilates.setter
    def valor_pilates(self, valor):
        if valor < 0:
            raise ValueError("O valor deve ser positivo.")
        self._valor_pilates = valor

    # property p/ obter o valor do funcional
    @property
    def valor_funcional(self):
        return self._valor_funcional

    # setter p/ definir que o valor do funcional seja apenas um valor positivo
    @valor_funcional.setter
    def valor_funcional(self, valor):
        if valor < 0:
            raise ValueError("O valor deve ser positivo.")
        self._valor_funcional = valor

# define a classe Aluno p/ guardar informações dos alunos
class Aluno:
    def __init__(self, cpf, nome, email, tipo_aula, professor, numero_aulas):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.tipo_aula = tipo_aula
        self.professor = professor
        self.numero_aulas = numero_aulas

    # property p/ calcular a mensalidade do aluno com base no tipo de aula e número de aulas
    @property
    def mensalidade(self):
        valor_professor = self.professor.valor_pilates if self.tipo_aula == "Pilates" else self.professor.valor_funcional
        custo_professor = valor_professor * (1 + 0.4 * (self.numero_aulas - 2))
        custo_estudio = custo_professor * 0.5
        return custo_professor + custo_estudio

# define a classe Estudio para gerenciar professores e alunos
class Estudio:
    def __init__(self):
        self.professores = {}  # lista para armazenar professores
        self.alunos = {}  # lista para armazenar alunos
        self.combobox = any  # placeholder do combobox (não usado diretamente)

    # método para adicionar um professor ao estúdio
    def adicionar_professor(self, professor):
        self.professores[professor.cpf] = professor

    # método para adicionar um aluno ao estúdio
    def adicionar_aluno(self, aluno):
        self.alunos[aluno.cpf] = aluno

    # método para consultar um aluno pelo CPF
    def consultar_aluno(self, cpf):
        return self.alunos.get(cpf)

    # método para calcular o faturamento de um professor pelo CPF
    def faturamento_professor(self, cpf):
        professor = self.professores.get(cpf)
        if not professor:
            return None
        valor_pilates = sum(aluno.mensalidade for aluno in self.alunos.values() if aluno.professor == professor and aluno.tipo_aula == "Pilates")
        valor_funcional = sum(aluno.mensalidade for aluno in self.alunos.values() if aluno.professor == professor and aluno.tipo_aula == "Funcional")
        return valor_pilates, valor_funcional

# função principal para criar a interface e gerenciar o estúdio
def main():
    estudio = Estudio()  # cria uma instância do Estudio

    # função para cadastrar um professor
    def cadastrar_professor():
        try:
            cpf = entry_prof_cpf.get()
            nome = entry_prof_nome.get()
            email = entry_prof_email.get()
            valor_pilates = float(entry_prof_valor_pilates.get())
            valor_funcional = float(entry_prof_valor_funcional.get())
            professor = Professor(cpf, nome, email, valor_pilates, valor_funcional)
            estudio.adicionar_professor(professor)
            combo_aluno_professor['values'] = list(estudio.professores.keys())  # atualização dos valores do combobox dos professores p/ fazer o cadastro de alunos
            messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    # função para cadastrar um aluno
    def cadastrar_aluno():
        try:
            cpf = entry_aluno_cpf.get()
            nome = entry_aluno_nome.get()
            email = entry_aluno_email.get()
            tipo_aula = combo_aluno_tipo_aula.get()
            professor_cpf = combo_aluno_professor.get()
            numero_aulas = int(combo_aluno_numero_aulas.get())
            professor = estudio.professores.get(professor_cpf)
            if not professor:
                raise ValueError("Professor não encontrado.")
            aluno = Aluno(cpf, nome, email, tipo_aula, professor, numero_aulas)
            estudio.adicionar_aluno(aluno)
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    # função para consultar um aluno pelo CPF
    def consultar_aluno():
        cpf = entry_consulta_cpf.get()
        aluno = estudio.consultar_aluno(cpf)
        if aluno:
            messagebox.showinfo("Consulta", f"Aluno: {aluno.nome}\nMensalidade: R${aluno.mensalidade:.2f}")
        else:
            messagebox.showerror("Erro", "Aluno não encontrado.")

    # função para calcular o faturamento de um professor pelo CPF
    def faturamento_professor():
        cpf = entry_fat_cpf.get()
        resultado = estudio.faturamento_professor(cpf)
        if resultado:
            valor_pilates, valor_funcional = resultado
            messagebox.showinfo("Faturamento", f"Valor Pilates: R${valor_pilates:.2f}\nValor Funcional: R${valor_funcional:.2f}")
        else:
            messagebox.showerror("Erro", "Professor não encontrado.")

    # criação da janela principal do tkinter
    root = tk.Tk()
    root.title("Estúdio de Treino")

    # frame para cadastro de professores
    frame_prof = tk.LabelFrame(root, text="Cadastro de Professores")
    frame_prof.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # campos de entrada para cadastro de professores
    tk.Label(frame_prof, text="CPF:").grid(row=0, column=0)
    entry_prof_cpf = tk.Entry(frame_prof)
    entry_prof_cpf.grid(row=0, column=1)

    tk.Label(frame_prof, text="Nome:").grid(row=1, column=0)
    entry_prof_nome = tk.Entry(frame_prof)
    entry_prof_nome.grid(row=1, column=1)

    tk.Label(frame_prof, text="Email:").grid(row=2, column=0)
    entry_prof_email = tk.Entry(frame_prof)
    entry_prof_email.grid(row=2, column=1)

    tk.Label(frame_prof, text="Valor Pilates:").grid(row=3, column=0)
    entry_prof_valor_pilates = tk.Entry(frame_prof)
    entry_prof_valor_pilates.grid(row=3, column=1)

    tk.Label(frame_prof, text="Valor Funcional:").grid(row=4, column=0)
    entry_prof_valor_funcional = tk.Entry(frame_prof)
    entry_prof_valor_funcional.grid(row=4, column=1)

    tk.Button(frame_prof, text="Cadastrar", command=cadastrar_professor).grid(row=5, columnspan=2)

    # frame para cadastro de alunos
    frame_aluno = tk.LabelFrame(root, text="Cadastro de Alunos")
    frame_aluno.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # campos de entrada para cadastro de alunos
    tk.Label(frame_aluno, text="CPF:").grid(row=0, column=0)
    entry_aluno_cpf = tk.Entry(frame_aluno)
    entry_aluno_cpf.grid(row=0, column=1)

    tk.Label(frame_aluno, text="Nome:").grid(row=1, column=0)
    entry_aluno_nome = tk.Entry(frame_aluno)
    entry_aluno_nome.grid(row=1, column=1)

    tk.Label(frame_aluno, text="Email:").grid(row=2, column=0)
    entry_aluno_email = tk.Entry(frame_aluno)
    entry_aluno_email.grid(row=2, column=1)

    tk.Label(frame_aluno, text="Tipo de Aula:").grid(row=3, column=0)
    combo_aluno_tipo_aula = ttk.Combobox(frame_aluno, values=["Pilates", "Funcional"])
    combo_aluno_tipo_aula.grid(row=3, column=1)

    tk.Label(frame_aluno, text="Professor:").grid(row=4, column=0)
    combo_aluno_professor = ttk.Combobox(frame_aluno, values=list(estudio.professores.keys()))
    combo_aluno_professor.grid(row=4, column=1)

    tk.Label(frame_aluno, text="Número de Aulas:").grid(row=5, column=0)
    combo_aluno_numero_aulas = ttk.Combobox(frame_aluno, values=[2, 3, 4])
    combo_aluno_numero_aulas.grid(row=5, column=1)

    tk.Button(frame_aluno, text="Cadastrar", command=cadastrar_aluno).grid(row=6, columnspan=2)

    # frame para consulta de alunos
    frame_consulta = tk.LabelFrame(root, text="Consulta de Alunos")
    frame_consulta.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # campos de entrada para consulta de alunos
    tk.Label(frame_consulta, text="CPF:").grid(row=0, column=0)
    entry_consulta_cpf = tk.Entry(frame_consulta)
    entry_consulta_cpf.grid(row=0, column=1)

    tk.Button(frame_consulta, text="Consultar", command=consultar_aluno).grid(row=1, columnspan=2)

    # frame para consulta de faturamento de professores
    frame_fat = tk.LabelFrame(root, text="Faturamento de Professores")
    frame_fat.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    # campos de entrada para consulta de faturamento de professores
    tk.Label(frame_fat, text="CPF:").grid(row=0, column=0)
    entry_fat_cpf = tk.Entry(frame_fat)
    entry_fat_cpf.grid(row=0, column=1)

    tk.Button(frame_fat, text="Consultar", command=faturamento_professor).grid(row=1, columnspan=2)

    # inicia o loop principal do tkinter
    root.mainloop()

# roda a função principal (executar diretamente)
if __name__ == "__main__":
    main()
