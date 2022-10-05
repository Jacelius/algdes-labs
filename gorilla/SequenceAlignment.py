# Helper function to print a matrix nicely
def show(intro, mat):
    print("\n" + intro)
    
    if isinstance(mat[0], int):
        print(mat)
        return 0

    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end = " " if j < m - 1 else "\n")

# read txt file data/BLOSUM62.txt, to add blosum to a dictionary
blosum = {}
with open('data/BLOSUM62.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if not line.startswith('#')]
    indexes = lines[0].split()
    # remove first index of each line

    for i in range(len(indexes)):
        blosum[indexes[i]] = {}
        l = lines[i+1].split()

        # remove first element of l (Since it's a letter)
        l.pop(0)
        for j in range(len(l)):
            blosum[indexes[i]][indexes[j]] = int(l[j])




with open('data/Toy_FASTAs-in.txt') as f:
    lines = f.readlines()

dna = {}
for line in lines:
    if ">" in line:  # new FASTA
        name = line.split()[0]
        dna_string = ""
    else:
        dna_string += line
        dna[name] = dna_string.strip('\n')


# time for the sequence alignment algorithm
"""
(6.16) The minimum alignment costs satisfy the following recurrence for i ≥ 1 and j ≥ 1:
opt(i, j) = min[ixiy + opt(i - 1, j - 1), 8 + opt(i - 1,j), 8 + opt(i, j - 1)].
Moreover, (i,j) is in an optimal alignment M for this subproblem if and only if the minimum is achieved by the first of these values.
We have maneuvered ourselves into a position where the dynamic programming algorithm has become clear: We build up the values of opt(i, j) using the recurrence in (6.16). There are only O(mn) subproblems, and OPT(m, n) is the value we are seeking.
We now specify the algorithm to compute the value of the optimal alignment. For purposes of initialization, we note that opt(i, 0) = opt(0, i) = iδ for all i, since the only way to line up an i-letter word with a 0-letter word is to use i gaps.
"""

print("dna dict", dna)

gap_penalty = blosum['*']['A'] # -4
double_gap_penalty = blosum['*']['*'] # 1

# helper function to print matrixes nicely
def show(intro, mat):
    print("\n" + intro)

    if isinstance(mat[0], int):
        print(mat)
        return 0

    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" " if j < m - 1 else "\n")

# def alignment(A, x, y):
#     # Fill in the rest of the matrix
#     for i in range(1, len(x)):  # 0 .. n
#         for j in range(1, len(y)):  # 0 .. m
#             A[i][j] = max( # we could be doing the traceback matrix here
#                 blosum[x[i]][y[j]] + A[i-1][j-1], # match/mismatch
#                 gap_penalty + A[i-1][j], # gap in x
#                 gap_penalty + A[i][j-1] # gap in y
#             )
#     return A[len(x)-1][len(y)-1]  # OPT(n, m)

# def fill_traceback_matrix(A):
#     # Initialize the traceback matrix
#     T = [[0 for j in range(len(y))] for i in range(len(x))]

#     # Define final cell in matrix
#     T[0][0] = "END"

#     # Initialize the first row and column
#     for i in range(1, len(x)):  # 1 .. n
#         T[i][0] = "UP"
#     for j in range(1, len(y)):  # 1 .. m
#         T[0][j] = "LEFT"
    
#     # Fill in the rest of the matrix
#     for i in range(1, len(x)):  # 0 .. n
#         for j in range(1, len(y)):  # 0 .. m
#             if A[i][j] == blosum[x[i]][y[j]] + A[i-1][j-1]:
#                 T[i][j] = "DIAG"
#             elif A[i][j] == gap_penalty + A[i-1][j]:
#                 T[i][j] = "UP"
#             elif A[i][j] == gap_penalty + A[i][j-1]:
#                 T[i][j] = "LEFT"
    
#     return T

# def traverse_traceback_matrix(T, x, y): # x and y are the sequences
#     # Initialize the aligned strings
#     x_aligned = ""
#     y_aligned = ""
#     # Start from the bottom right cell in the traceback matrix
#     i = len(x) - 1
#     j = len(y) - 1
#     # Keep going until you reach the top left cell
#     while T[i][j] != "END":
#         if T[i][j] == "DIAG":
#             x_aligned = x[i] + x_aligned
#             y_aligned = y[j] + y_aligned
#             i -= 1
#             j -= 1
#         elif T[i][j] == "UP":
#             x_aligned = x[i] + x_aligned
#             y_aligned = "-" + y_aligned
#             i -= 1
#         elif T[i][j] == "LEFT":
#             x_aligned = "-" + x_aligned
#             y_aligned = y[j] + y_aligned
#             j -= 1
#     return x_aligned, y_aligned


def create_2d_array(x, y):
    return [[0 for i in range(len(x)+1)] for j in range(len(y)+1)] 


def fill_gp(arr):
    for i in range(1, len(arr)+1): # fill column with gps
        arr[0][i] = gap_penalty * i
        for j in range(i):
            arr[j][0] = gap_penalty * j

def alignment2(A, x, y): # x and y are the sequences as strings
    for i in range(1, len(A)): # loop over length of row
        for j in range(1, len(A[0])): # loop over length of column
                A[i][j] = max(
                    A[i-1][j-1] + blosum[y[i-1]][x[j-1]],
                    A[i-1][j] + gap_penalty,
                    A[i][j-1] + gap_penalty
                )

def getSmallerDna(dna1, dna2):
    if len(dna1) >= len(dna2):
        return dna1, dna2
    return dna2, dna1

x,y = getSmallerDna(dna['>Sphinx'], dna['>Bandersnatch']) 


max_size = max(len(x)+1, len(y)+1)
A = create_2d_array(x, y)  # initialize A (The 2d array of scores)
T = create_2d_array(x, y)  # initialize A (The 2d array of scores)

fill_gp(A) # fill the first row and column with gap penalties

alignment2(A, x, y)

show("A", A)

""" for key in dna:
    # mix with all other dna's
    reduced_dna = dna.copy()
    reduced_dna.pop(key)
    for other in reduced_dna:
        x = dna[key]
        y = reduced_dna[other]
        max_size = max(len(x), len(y))
        A = [[gap_penalty]*max_size for i in range(max_size)] # initialize A
        mn = alignment(A, x, y)
        show("A for " + key +  " with " + other, A)
        print("A[m][n]", mn)
        # Work backwards from (N - 1, M - 1) to (0, 0)
        # to find the best alignment.
        T = fill_traceback_matrix(A)
        show("T for " + key +  " with " + other, T)
         x_aligned, y_aligned = traverse_traceback_matrix(T, x, y)
        print("x_aligned", x_aligned)
        print("y_aligned", y_aligned) """
        



