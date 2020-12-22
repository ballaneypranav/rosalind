from Bio import SeqIO

def main():
    reads = []
    for record in SeqIO.parse('rosalind_long.txt', "fasta"):
        reads.append((str(record.seq), "unused"))

    superstring = reads[0][0]
    reads[0] = (superstring, "used")

    use_count = 1
    while use_count < len(reads):
        for i in range(len(reads)):
            
            read, status = reads[i]
            if status == "used":
                continue

            half = len(read) // 2
            head = superstring[: half+1]
            tail = superstring[-half-1 : ]

            if head in read:
                index = read.find(head)
                potential_head = read[index:]
                if superstring.find(potential_head) == 0:
                    superstring = read[:index] + superstring
                reads[i] = (read, "used")
                use_count += 1
                continue

            if tail in read:
                index = read.find(tail)
                potential_tail = read[: index + half + 1]
                if superstring.find(potential_tail) + len(potential_tail) == len(superstring):
                    superstring = superstring + read[index+half+1:]
                reads[i] = (read, "used")
                use_count += 1
                continue
        
    print(superstring)

if __name__ == "__main__":
    main()





