# read txt file data/BLOSUM62.txt

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

dna = {}

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

scoring_matrix = []

def
