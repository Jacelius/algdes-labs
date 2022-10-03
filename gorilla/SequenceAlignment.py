# read txt file data/BLOSUM62.txt, to add scores to a dictionary
scores = {}
with open('data/BLOSUM62.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if not line.startswith('#')]
    indexes = lines[0].split()
    # remove first index of each line

    for i in range(len(indexes)):
        scores[indexes[i]] = {}
        l = lines[i+1].split()

        # remove first element of l (Since it's a letter)
        l.pop(0)
        for j in range(len(l)):
            scores[indexes[i]][indexes[j]] = int(l[j])


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
(6.16)   The minimum alignment costs satisfy the following recurrence for i ≥ 1 and j ≥ 1:
opt(i, j) = min[ixiy + opt(i - 1, j - 1), 8 + opt(i - 1,j), 8 + opt(i, j - 1)].
Moreover, (i,j) is in an optimal alignment M for this subproblem if and only if the minimum is achieved by the first of these values.
 
We have maneuvered ourselves into a position where the dynamic programming algorithm has become clear: We build up the values of opt(i, j) using the recurrence in (6.16). There are only O(mn) subproblems, and OPT(m, n) is the value we are seeking.
We now specify the algorithm to compute the value of the optimal alignment. For purposes of initialization, we note that opt(i, 0) = opt(0, i) = iδ for all i, since the only way to line up an i-letter word with a 0-letter word is to use i gaps.
"""

# define 2d grid: scoring matrix

print(dna)

gap_penalty = scores['*']['A']
double_gap_penalty = scores['*']['*']


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


def opt(x: list, y: list):  # (6.16) Needleman Wunsch algorithm

    max_length = max(len(x), len(y))


def alignment(x, y):
    max_size = max(len(x), len(y))
    # dimensions: len(x) * len(y)
    A = [[gap_penalty]*max_size for i in range(max_size)]
    # Initialize A[i, 0] for each i
    for i in range(len(x)):
        A[i][0] = i * gap_penalty  # 8 is the gap penalty (fix)
    # Initialize A[0, j] for each j
    for j in range(len(y)):
        A[0][j] = j * gap_penalty  # 8 is the gap penalty (fix)
    # Fill in the rest of the matrix
    for i in range(len(x)):  # 0 .. n
        for j in range(len(y)):  # 0 .. m
            A[i][j] = max(
                scores[x[i]][y[j]] + A[i-1][j-1],
                gap_penalty + A[i-1][j],
                gap_penalty + A[i][j-1]
            )
    return A  # OPT(n, m)


for key in dna:
    # mix with all other dna's
    reduced_dna = dna.copy()
    reduced_dna.pop(key)
    for other in reduced_dna:
        #x = list(dna[key])
        #y = list(dna[other])
        print(alignment(dna[key], dna[other]))
