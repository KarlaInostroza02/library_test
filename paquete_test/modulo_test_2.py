import numpy as np

from .modulo_test import operaciones_aritmeticas

class product_matrix(operaciones_aritmeticas):
    def __init__(self):
        pass

    def product_matriz(self, A, B):

        row_a, columns_a = A.shape
        row_b, columns_b = B.shape

        if columns_a == row_b:
                C = np.zeros((row_a, columns_b))
                for i in range(row_a ):
                    for j in range(columns_b):
                        for k in range(len(B)):
                            C[i][j] = operaciones_aritmeticas.producto(self, A[i][k], B[k][j])

        #try:
        #except:
        #    print("No se puede realizar producto de matrices")

        return C