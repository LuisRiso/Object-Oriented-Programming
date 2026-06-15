class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.valida_criterios()  # Chamado automaticamente nas subclasses

    def valida_criterios(self):
        raise NotImplementedError("Cada subclasse deve implementar validação de critérios.")

    def printDescricao(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, titulacao):
        self.titulacao = titulacao
        super().__init__(nome, idade, cpf)

    def valida_criterios(self):
        if self.titulacao.lower() != "doutor":
            raise ValueError(f"Erro: Professor {self.nome} deve ter titulação 'Doutor'.")
        if self.idade < 30:
            raise ValueError(f"Erro: Professor {self.nome} deve ter idade igual ou maior que 30 anos.")

    def printDescricao(self):
        print(f"Professor: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Titulação: {self.titulacao}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, curso):
        self.curso = curso
        super().__init__(nome, idade, cpf)

    def valida_criterios(self):
        if self.curso not in ["CCO", "SIN"]:
            raise ValueError(f"Erro: Aluno {self.nome} deve estar no curso 'CCO' ou 'SIN'.")
        if self.idade < 18:
            raise ValueError(f"Erro: Aluno {self.nome} deve ter idade igual ou maior que 18 anos.")

    def printDescricao(self):
        print(f"Aluno: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Curso: {self.curso}")

class Cadastro:
    def __init__(self):
        self.pessoas = {}
    
    def adicionar_pessoa(self, pessoa):
        if pessoa.cpf in self.pessoas:
            raise ValueError(f"Erro: Já existe uma pessoa cadastrada com o CPF {pessoa.cpf}.")
        self.pessoas[pessoa.cpf] = pessoa

    def listar_pessoas(self):
        for pessoa in self.pessoas.values():
            pessoa.printDescricao()

# Fábrica de Pessoas
def criar_pessoa(tipo, nome, idade, cpf, extra):
    if tipo == "Professor":
        return Professor(nome, idade, cpf, extra)
    elif tipo == "Aluno":
        return Aluno(nome, idade, cpf, extra)
    else:
        raise ValueError("Tipo de pessoa desconhecido")

# Exemplo de uso
def main():
    cadastro = Cadastro()

    # Lista de dados para criação de pessoas
    pessoas_dados = [
        ("Professor", "Dr Carlos", 40, "12345678901", "Doutor"),
        ("Professor", "Dr Ana", 29, "23456789012", "Doutor"),  # Deve gerar erro (idade < 30)
        ("Aluno", "Pedro", 20, "34567890123", "CCO"),
        ("Aluno", "Maria", 17, "45678901234", "SIN"),          # Deve gerar erro (idade < 18)
        ("Aluno", "João", 22, "56789012345", "ENG")            # Deve gerar erro (curso != CCO ou SIN)
    ]

    for tipo, nome, idade, cpf, extra in pessoas_dados:
        try:
            pessoa = criar_pessoa(tipo, nome, idade, cpf, extra)
            cadastro.adicionar_pessoa(pessoa)
        except ValueError as e:
            print(e)  # Exibe o erro e permite que o loop continue

    print("\nCadastro resultante:")
    cadastro.listar_pessoas()

if __name__ == "__main__":
    main()
