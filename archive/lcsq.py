from Bio import SeqIO

from sys import setrecursionlimit
setrecursionlimit(2000)


def main():
    sequences = []
    for record in SeqIO.parse('rosalind_lcsq.txt', "fasta"):
        sequences.append(str(record.seq))
    
    s, t = sequences[0], sequences[1]

    archive = {}
    result, archive = LCS(s, t, archive)
    print(result)

def LCS(s, t, archive):
    if s == '' or t == '':
        return ('', archive)
    elif (s, t) in archive.keys():
        return (archive[(s, t)], archive)
    elif s[-1] == t[-1]:
        result, archive = LCS(s[:-1], t[:-1], archive)
        result += s[-1]
        archive[(s, t)] = result
        return (result, archive)
    else:
        one, archive = LCS(s[:-1], t, archive)
        two, archive = LCS(s, t[:-1], archive)
        result = longer(one, two)
        archive[(s, t)] = result
        return (result, archive)

def longer(s, t):
    if len(s) >= len(t):
        return s
    else:
        return t


if __name__ == "__main__":
    main()
