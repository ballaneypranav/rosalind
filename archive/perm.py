from copy import copy

# n = int(input())
n = 7


def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)
print(factorial(n))

numbers = [x+1 for x in range(n)]

def generate_permutations(numbers):
    if len(numbers) == 1:
        return [numbers]

    permutations = []
    for number in numbers:
        numbers_copy = copy(numbers)
        numbers_copy.remove(number)
        for permutation in generate_permutations(numbers_copy):
            permutations.append([number] + permutation)
    
    return permutations

for permutation in generate_permutations(numbers):
    print(*permutation)