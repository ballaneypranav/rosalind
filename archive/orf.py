from Bio import SeqIO

def main():
    sequence = ""
    for record in SeqIO.parse('rosalind_orf.txt', "fasta"):
        sequence = str(record.seq)

    frames = ORFs(sequence)
    proteins = set()
    for frame in frames:
        codons = tokenize(frame)
        translated = translate(codons)
        for i in range(len(translated)):
            protein = ""
            if translated[i] == 'M':
                protein += 'M'
                for j in range(i+1, len(translated)):
                    protein += translated[j]
                    if translated[j] == '_':
                        break
                if protein[-1] == '_':
                    proteins.add(protein[:-1])

    for protein in proteins:
        print(protein)

                


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

def ORFs(seq):
    frames = []
    frames.append(seq)
    frames.append(seq[1:])
    frames.append(seq[2:])
    frames.append(reverse_complement(seq))
    frames.append(reverse_complement(seq[:-1]))
    frames.append(reverse_complement(seq[:-2]))

    return frames


def reverse_complement(seq):
    result = ""
    for base in seq[::-1]:
        if base == 'A':
            result += 'T'
        elif base == 'T':
            result += 'A'
        elif base == 'C':
            result += 'G'
        elif base == 'G':
            result += 'C'
    return result

if __name__ == "__main__":
    main()