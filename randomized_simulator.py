# Generates random inputs for a problem, then
# runs two Python scripts with the same inputs
# and compares the result.

import subprocess
import random

RANGE = 100
A = 3
B = 100

def main():

    for i in range(RANGE):
        n = random.randint(A, B)
        numbers = list(range(n))
        random.shuffle(numbers)

        with open('random_input', 'w') as file:
            file.write(str(n) + '\n')
            for item in numbers:
                file.write("%s " % item)

        with open('random_input', 'r') as file:
            custom = subprocess.run(
                ["python3.7", "mmch.py"], stdin=file, capture_output=True)
            custom = str(custom.stdout, encoding="UTF8").strip()

        solution = MM(seq)

        match = check(custom, solution)

        if not match:
            print("Input: ")
            print(n)
            print(numbers)
            print("Attempt:")
            print(custom)
            print("Solution:")
            print(solution)
            exit(1)
        else:
            print(f"Attempt {i+1} successful.")


def check(custom, solution):
    custom = custom.split('\n')
    solution = solution.split('\n')

    custom[0] = [int(x) for x in custom[0].split(' ')]
    custom[1] = [int(x) for x in custom[1].split(' ')]
    solution[0] = [int(x) for x in solution[0].split(' ')]
    solution[1] = [int(x) for x in solution[1].split(' ')]

    result = (len(custom[0]) == len(solution[0])) and (len(custom[1]) == len(solution[1]))

    if not result:
        print((len(custom[0]), len(solution[0]), len(custom[1]), len(solution[1])))

    return result


if __name__ == "__main__":
    main()

def MM(seq):
    A = seq.count('A')
    U = seq.count('U')
    C = seq.count('C')
    G = seq.count('G')
    
    if A > U:
        MMAU = factorial(A)/factorial(A-U)
    else:
        MMAU = factorial(U)/factorial(U-A)
    if C > G:
        MMGC = factorial(C)/factorial(C-G)
    else:
        MMGC = factorial(G)/factorial(G-C)
    return MMAU*MMGC