class Pessoa:
	def __init__(self, nome, sexo, cpf, ativo):
		self.nome = nome
		self.sexo= sexo
		self.cpf = cpf
		self.ativo = ativo
		
	def desativar(self):
		self.ativo = False

if __name__ == "__main__":
			pessoa1 = Pessoa("Iasmin", 'F', '626267', True)
			pessoa1.desativar()
			print(pessoa1.nome)
