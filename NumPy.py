import numpy as np
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matriz original")
print(matrix)
element=matrix
print("\nElemento na segunda linha, terceira coluna:\n", element)
result=matrix+10
print("\nMatriz após adição de 10:\n", result)
result=np.multiply(matrix, 2)
print("\nMatriz após multiplicação por 2:\n", result)
matrix2=np.array([[0,0,0],[0,0,0],[0,0,0]])
print("\nProduto das matrizes:\n", matrix2)
