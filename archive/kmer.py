from Bio import SeqIO

def main():
    alphabet = "ACGT"
    n = 4

    count = {}

    permutations = generate_permutations(alphabet, n)

    for permutation in permutations:
        count[permutation] = 0
    
    sequence = ""
    for record in SeqIO.parse('rosalind_kmer.txt', "fasta"):
        sequence = str(record.seq)

    for i in range(len(sequence)-3):
        count[sequence[i:i+4]] += 1

    for permutation in permutations:
        print(count[permutation], end=' ')

def generate_permutations(alphabet, length):
    if length == 0:
        return [""]

    permutations = []

    sub_permutations = generate_permutations(alphabet, length-1)

    for letter in alphabet:
        for permutation in sub_permutations:
            permutations.append(letter + permutation)
    
    return permutations


if __name__ == "__main__":
    main()