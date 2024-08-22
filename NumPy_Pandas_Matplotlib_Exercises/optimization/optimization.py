import numpy as np

def simplex(A, b, C):
    m, n = np.array(A).shape
    
    # Initialization
    Basis = np.arange(n)
    B = A[:, Basis]
    CB = C[Basis]
    eps = 1e-12

    while True:
        RC = CB - np.dot(np.dot(CB, np.linalg.inv(B)), A)
        if np.all(RC <= eps):
            X = np.zeros(n)
            X[Basis] = np.dot(np.linalg.inv(B), b)
            Z = np.dot(C, X)
            return int(np.round(Z)), list(np.round(X).astype(int))
        entering_var = np.argmax(RC)
        d = np.dot(np.linalg.inv(B), A[:, entering_var])
        if np.all(d <= eps):
            print("Problem is unbounded.")
            return None, None
        ratios = np.divide(X[Basis], d)
        ratios[d <= 0] = np.inf
        leaving_var_idx = np.argmin(ratios)
        leaving_var = Basis[leaving_var_idx]
        Basis[leaving_var_idx] = entering_var
        B = A[:, Basis]
        CB = C[Basis]

# Test the function with given matrices
A = np.array([[1, 2, 1], [3, 0, 2], [1, 4, 0]])
b = np.array([430, 460, 400])
C = np.array([3000, 2000, 5000])

print(simplex(A, b, C))