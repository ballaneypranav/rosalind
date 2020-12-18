from Bio import SeqIO

sequence = ""
for record in SeqIO.parse('rosalind_pmch.txt', "fasta"):
    sequence = str(record.seq)

count_A = 0
count_C = 0

for base in sequence:
    if base == 'A':
        count_A += 1
    elif base == 'C':
        count_C += 1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(count_A) * factorial(count_C))