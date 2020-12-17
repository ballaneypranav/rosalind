from Bio import SeqIO

matrix = {'A': [], 'C': [], 'G': [], 'T': []}

for record in SeqIO.parse('rosalind_cons.txt', "fasta"):
    seq = str(record.seq)
    n = len(seq)
    
    if matrix['A'] == []:
        for key in matrix:
            matrix[key] = [0] * n
    
    for i in range(len(seq)):
        base = seq[i]
        matrix[base][i] += 1

n = len(matrix['A'])
for i in range(n):
    maximum = 0
    max_key = 'x'
    for key in matrix.keys():
        if matrix[key][i] > maximum:
            maximum = matrix[key][i]
            max_key = key
    print(max_key, end='')

print()
for key in matrix.keys():
    print(key + ': ', end='')
    print(*(matrix[key]))

