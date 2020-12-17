from Bio import SeqIO

sequences = []
for record in SeqIO.parse('rosalind_lcsm.txt', "fasta"):
    sequences.append(str(record.seq))

common_sequences = []

for i in range(len(sequences[0])):
    for j in range(i, len(sequences[0])):
        substr = sequences[0][i:j+1]

        common = True
        for sequence in sequences:
            if substr not in sequence:
                common = False
                break
        if common:
            common_sequences.append(substr)

max = 0
seq = ""
for sequence in common_sequences:
    if len(sequence) > max:
        max = len(sequence)
        seq = sequence
print(seq)