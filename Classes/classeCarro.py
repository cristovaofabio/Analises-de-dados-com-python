'''class Carro(object):
	pass

palio = Carro()
print(type(palio))'''

'''class Estudantes:
	def __init__(self, nome,idade,nota):
		self.nome=nome
		self.idade=idade
		self.nota=nota
Estudante1 = Estudantes("cristovao",21,9.3)
print(Estudante1.nome)
print(hasattr(Estudante1,"nome"))'''

'''class Circulo(object):
	pi=3.14
	def __init__(self,raio=5):
		self.raio=raio
	def area(self):
		return (self.raio*self.raio)*Circulo.pi
	def setRaio(self,novo_raio):
		self.raio=novo_raio
	def getRaio(self):
		return self.raio
circ = Circulo()
print("Raio inicial: %d"%circ.getRaio())
circ.setRaio(8)
print("Novo raio: %d"%circ.getRaio())
print("Area do circulo: %d"%circ.area())'''

#heranca em python

'''class Animal(object):
	def __init__(self):
		print("Classe animal criada")
	def Indentif(self):
		print("Animal")
	def comer(self):
		print("Comendo")

class Cachorro(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Objeto cachorro criado")
	def Indentif(self):
		print("Cachorro")
	def latir(self):
		print("Au au")

boby = Cachorro()
print(boby.comer())'''

#metodos especiais

class Livro(object):
	def __init__(self,titulo,autor,paginas):
		print("Livro criado")
		self.titulo=titulo
		self.autor=autor
		self.paginas=paginas
	def __str__(self):
		return "Titulo: %s, autor: %s, paginas: %s"%(self.titulo,self.autor,self.paginas)
	def __len__(self):
		return self.paginas
livro1 = Livro("Odisseia","Homero",1500)
print(livro1)
print(len(livro1))
