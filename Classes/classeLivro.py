class Livro():

	def __init__(self,titulo,isbn):
		self.titulo=titulo
		self.isbn=isbn
		print('Construtor chamado para criar um objeto desta classe')
	def imprime(self):
		print("Foi criado o livro %s e ISBN %d"%(self.titulo,self.isbn))

Livro1=Livro("A menina que roubava livros",32779423)
Livro1.imprime()

class Cachorro():
	def __init__(self,raca):
		self.raca=raca
		print("Classe cachorro construida!")

Rex = Cachorro('Labrador')
print(Rex.raca)
ids=[1,2,4,6]
valores=[6,3,9,1]
plt.bar(ids,valores)
plt.show()
