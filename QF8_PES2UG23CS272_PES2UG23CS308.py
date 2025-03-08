import numpy as np
from numpy.linalg import matrix_rank

def compute_rank_and_nullity(A):
    """
    Computes the rank and nullity of a matrix A.
    """ 
    rank=matrix_rank(A)
    nullity=A.shape[1]-rank
    return rank,nullity

# Read input
m, n= map(int, input().split())
A =[]
for _ in range(m):
    row = list(map(int, input().split()))
    A.append(row)

# Convert to numpy array
A = np.array(A)

# Compute rank and nullity
rank, nullity = compute_rank_and_nullity(A)

# Print the result
print(rank, nullity)