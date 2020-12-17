import requests
from Bio import SeqIO
import re

pattern = r'(?=N[^P][ST][^P])'

with open('rosalind_mprt.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    fasta = requests.get('https://www.uniprot.org/uniprot/' + line + '.fasta').text
    with open('data/' + line + '.fasta', 'w') as file:
        file.write(fasta)
    for record in SeqIO.parse('data/' + line + '.fasta', "fasta"):
        locations = [m.start() + 1 for m in re.finditer(pattern, str(record.seq))]
        if locations != []:
            print(line)
            print(*locations)

    