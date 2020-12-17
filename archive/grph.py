with open('rosalind_grph.txt', 'r') as file:
    lines = file.readlines()

sequences = {}
key = ""
for line in lines:
    line = line.strip()
    if line[0] == '>':
        key = line[1:]
        sequences[key] = ""
    else:
        sequences[key] += line

for key1 in sequences.keys():
    seq1 = sequences[key1]
    suffix = seq1[-3:]
    for key2 in sequences.keys():
        seq2 = sequences[key2]
        prefix = seq2[:3]
        if suffix == prefix and seq1 != seq2:
            print(key1 + " " + key2)
