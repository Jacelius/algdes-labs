# Helper function to print a matrix nicely -- Thank you Lorenzo404
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

i = input("Press 1 to run HbB and any other key to run Toy: ")
if i == '1':
    with open('data/HbB_FASTAs-in.txt') as f:
        lines = f.readlines()
else:
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

def create_2d_array(x, y):
    return [[0 for i in range(len(x)+1)] for j in range(len(y)+1)] 

def getBiggerDna(dna1, dna2):
    if len(dna1) >= len(dna2):
        return dna1.strip(), dna2.strip()
    return dna2.strip(), dna1.strip()

def max_traceback(A, T, x, y, i, j):
    maxvalue = max(
        A[i-1][j-1] + blosum[y[i-1]][x[j-1]],
        A[i-1][j] + gap_penalty,
        A[i][j-1] + gap_penalty
    )
    
    if maxvalue == A[i-1][j-1] + blosum[y[i-1]][x[j-1]]:
        T[i][j] = 'Diag'
    elif maxvalue == A[i-1][j] + gap_penalty:
        T[i][j] = 'Up'
    else:
        T[i][j] = "Left"

    return maxvalue

def fill_traversal(arr):
    for i in range(len(arr[0])): # fill column with gps
        arr[0][i] = 'Left'
        for j in range(len(arr)):
            arr[j][0] = 'Up'
    arr[0][0] = 'Done'

def fill_gp(arr):
    for i in range(1, len(arr[0])): # fill column with gps
        arr[0][i] = gap_penalty * i
        for j in range(len(arr)):
            arr[j][0] = gap_penalty * j

# fill up A
def alignment(A, T, x, y): # x and y are the sequences as strings
    for i in range(1, len(A)): # loop over length of row
        for j in range(1, len(A[0])): # loop over length of column
                A[i][j]= max_traceback(A, T, x, y, i, j)
    return A[len(A)-1][len(A[0])-1]

def traversal(T, s, i, j):
    # build up string alignment from T matrix
    next_step = T[i][j]

    if next_step == "Left":
        traversal(T, "-" + s, i, j-1)
    elif next_step == "Up":
        traversal(T, "-" + s, i-1, j)
    elif next_step == "Diag":
        traversal(T, y[i-1] + s, i-1, j-1)
    else:
        print(y)
        print(s) 


gap_penalty = blosum['*']['A'] # -4
double_gap_penalty = blosum['*']['*'] # 1

keys = []

# removes all new lines in that shitty input file >:(
for key in dna:
    keys.append(key)
    val = dna[key]
    dna[key] = val.replace('\n', '')

print('Available inputs: ' + str(keys))
x_name = input("Choose first subject: ")
y_name = input("Choose second subject: ")

x_name = '>' + x_name.lower().replace('>', '').capitalize()
y_name = '>' + y_name.lower().replace('>', '').capitalize()

x,y = getBiggerDna(dna[x_name], dna[y_name]) 

max_size = max(len(x)+1, len(y)+1)
A = create_2d_array(x, y)  # initialize A (The 2d array of scores)
T = create_2d_array(x, y)  # initialize A (The 2d array of scores)

fill_gp(A) # fill the first row and column with gap penalties 
fill_traversal(T)

mn = alignment(A, T, x, y)

print(f"{x_name[1:]}--{y_name[1:]} score = {str(mn)}")
traversal(T, '', len(T)-1, len(T[0])-1)


show("A", A)
show("T", T)