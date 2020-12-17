from Bio import SeqIO

def main():
    sequences = []
    for record in SeqIO.parse('rosalind_splc.txt', "fasta"):
        sequences.append(str(record.seq))

    for sequence in sequences[1:]:
        sequences[0] = "".join(sequences[0].split(sequence))

    sequence = sequences[0]

    codons = tokenize(sequence)
    translated = translate(codons)
    for i in range(len(translated)):
        protein = ""
        if translated[i] == 'M':
            protein += 'M'
            for j in range(i+1, len(translated)):
                if translated[j] == '_':
                    print(protein)
                    exit(0)
                protein += translated[j]


def translate(codons):
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 

    translated_seq = ""
    for codon in codons:
        translated_seq += table[codon]

    return translated_seq


def tokenize(seq):
    tokens = []
    for i in range(0, len(seq), 3):
        if i+3 <= len(seq):
            tokens.append(seq[i:i+3])
    return tokens

if __name__ == "__main__":
    main()