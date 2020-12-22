from copy import copy 

n = int(input())
numbers = [x+1 for x in range(n)]

def generate_permutations(numbers):
    if len(numbers) == 1:
        return [[-1 * numbers[0]], [numbers[0]]]

    permutations = []
    for number in numbers:
        numbers_copy = copy(numbers)
        numbers_copy.remove(number)
        for permutation in generate_permutations(numbers_copy):
            permutations.append([-1 * number] + permutation)
            permutations.append([number] + permutation)
    
    return permutations

permutations = generate_permutations(numbers)

print(len(permutations))
for permutation in permutations:
    print(*permutation)