# read txt file data/BLOSUM62.txt
with open('data/BLOSUM62.txt') as f: 
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if not line.startswith('#')]
    BLOSUM62 = [line.split() for line in lines]

dna = {}

with open('data/Toy_FASTAs-in.txt') as f: 
    lines = f.readlines()

dna = {}
for line in lines:
    if ">" in line: # new FASTA
        name = line.split()[0]
        dna_string = ""
    else:
        dna_string += line
        dna[name] = dna_string.strip('\n')

# time for the sequence alignment algorithm

scoring_matrix = []
