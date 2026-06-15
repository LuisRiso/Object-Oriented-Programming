class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def printDescricao(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, titulacao):
        super().__init__(nome, idade, cpf)
        self.titulacao = titulacao
        self.valida_criterios()

    def valida_criterios(self):
        if self.titulacao.lower() != "doutor":
            raise ValueError(f"Erro: Professor {self.nome} deve ter titulação 'Doutor'.")
        if self.idade < 30:
            raise ValueError(f"Erro: Professor {self.nome} deve ter idade igual ou maior que 30 anos.")

    def printDescricao(self):
        print(f"Professor: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Titulação: {self.titulacao}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, curso):
        super().__init__(nome, idade, cpf)
        self.curso = curso
        self.valida_criterios()

    def valida_criterios(self):
        if self.curso not in ["CCO", "SIN"]:
            raise ValueError(f"Erro: Aluno {self.nome} deve estar no curso 'CCO' ou 'SIN'.")
        if self.idade < 18:
            raise ValueError(f"Erro: Aluno {self.nome} deve ter idade igual ou maior que 18 anos.")

    def printDescricao(self):
        print(f"Aluno: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Curso: {self.curso}")

class Cadastro:
    def __init__(self):
        self.pessoas = []
        self.cpfs = set()

    def adicionar_pessoa(self, pessoa):
        if pessoa.cpf in self.cpfs:
            raise ValueError(f"Erro: Já existe uma pessoa cadastrada com o CPF {pessoa.cpf}.")
        self.cpfs.add(pessoa.cpf)
        self.pessoas.append(pessoa)

    def listar_pessoas(self):
        for pessoa in self.pessoas:
            pessoa.printDescricao()

# Exemplo de uso
def main():
    cadastro = Cadastro()

    # Lista de pessoas com alguns dados inválidos
    pessoas_dados = [
        ("Professor", "Dr Carlos", 40, "12345678901", "Doutor"),
        ("Professor", "Dr Ana", 29, "23456789012", "Doutor"),    # Inválido (idade < 30)
        ("Professor", "Dr Paulo", 45, "67890123456", "Mestre"),  # Inválido (titulação != Doutor)
        ("Professor", "Dr Julia", 50, "78901234567", "Doutor"),  # Válido
        ("Aluno", "Pedro", 20, "34567890123", "CCO"),      # Válido
        ("Aluno", "Maria", 17, "45678901234", "SIN"),          # Inválido (idade < 18)
        ("Aluno", "João", 22, "56789012345", "ENG"),             # Inválido (curso != CCO ou SIN)
        ("Aluno", "Alice", 19, "89012345678", "SIN"),            # Válido
        ("Professor", "Dr Roberto", 34, "12389045601", "Doutor"),  # Válido
        ("Professor", "Dr Helena", 32, "45612378901", "Doutor"),      # Válido
        ("Aluno", "Lucas", 25, "78945612302", "CCO"),                 # Válido
        ("Aluno", "Beatriz", 18, "23456789001", "SIN")            # Válido
    ]

    for tipo, nome, idade, cpf, extra in pessoas_dados:
        try:
            if tipo == "Professor":
                pessoa = Professor(nome, idade, cpf, extra)
            elif tipo == "Aluno":
                pessoa = Aluno(nome, idade, cpf, extra)
            cadastro.adicionar_pessoa(pessoa)
        except ValueError as e:
            print(e)  # Exibe o erro e permite que o loop continue

    print("\nCadastro resultante:")
    cadastro.listar_pessoas()

if __name__ == "__main__":
    main()
