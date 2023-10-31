#Classe Node para representar um nó da Árvore
class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
	def add_child(self, child_node):
		self.children.append(child_node)
#Criando uma Árvore de exemplo
root = Node("A")
root.add_child(Node("B"))
root.add_child(Node("C"))
root.children[1].add_child(Node("D"))
root.children[1].add_child(Node("E"))
root.children[1].add_child(Node("F"))
#Exibindo a Árvore
print("Árvore de Exemplo")
print(root.value)
for child in root.children:
	print("¬", child.value)
	for grandchild in child.children:
		print("¬", grandchild.value)
