alphabet = input().split()
n = int(input())

def generate_permutations(alphabet, length):
    if length == 0:
        return [""]

    permutations = []

    sub_permutations = [''] + generate_permutations(alphabet, length-1)

    for letter in alphabet:
        for permutation in sub_permutations:
            if letter + permutation not in permutations:
                permutations.append(letter + permutation)
    
    return permutations

for permutation in generate_permutations(alphabet, n):
    print(permutation)