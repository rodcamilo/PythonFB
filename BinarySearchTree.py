class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if  value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    def search(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left is not None:
                return self.right.search(value)
            else:
                return False
        if value > self.value:
            if self.right is not None:
                return self.right.search(value)
            else:
                return False
bst = BinarySearchTree(50)
bst.insert(30)
bst.insert(40)
bst.insert(50)
bst.insert(60)
bst.insert(70)
print("Busca 30:", bst.search(30))
print("Busca 40:", bst.search(40))
print("Busca 50:", bst.search(50))
print("Busca 60:", bst.search(60))
print("Busca 70:", bst.search(70))
