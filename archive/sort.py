# from copy import copy
def main():
    initial = [0] + [int(x) for x in input().split()] + [11]
    final   = [0] + [int(x) for x in input().split()] + [11]
    
    inversions = minimum_inversions(initial, final)
    print(len(inversions))
    for inversion in inversions:
        print(inversion[0], inversion[1])

calculated_results = {}

def minimum_inversions(initial, final):
    """Recursively calculates the minimum number of inversions 
    to convert the initial array to the final array."""
    initial_s = string(initial)
    final_s = string(final)

    if (initial_s, final_s) in calculated_results.keys():
        return calculated_results[(initial_s, final_s)]    
    
    neighbours = find_neighbours(final)
    breaks = find_breaks(initial, neighbours)

    # print(breaks)

    if breaks == []:
        return []

    # count resolutions if the sequence between any two
    # pair of breaks is flipped
    resolutions = {0: [], 1: [], 2: []}

    for i in range(len(breaks)-1):
        for j in range(i+1, len(breaks)):
            # if the breaks are next to each other, 
            # it is impossible to resolve them by flipping the two
            # since there is only one element in the middle
            if breaks[i][1] == breaks[j][0]:
                continue
            else:
                # count the number of resulutions if the sequence
                # between these breaks is flipped
                count = 0
                if (breaks[i][0], breaks[j][0]) in neighbours:
                    count += 1
                if (breaks[i][1], breaks[j][1]) in neighbours:
                    count += 1

                resolutions[count].append((breaks[i], breaks[j]))

    inversions = {}

    for i in [2, 1, 0]:
        for A, B in resolutions[i]:
            reversed = reverse(initial, A, B)
            # get indices of A[1] and B[0]
            x, y = 0, 0
            for i in range(len(initial)):
                if initial[i] == A[1]:
                    x = i
                if initial[i] == B[0]:
                    y = i
            inversions[(A, B)] = [(x, y)] + minimum_inversions(reversed, final)

        if inversions != {}:
            minimum_key = list(inversions.keys())[0]
            minimum = len(inversions[minimum_key])
            for key in inversions.keys():
                if len(inversions[key]) < minimum:
                    minimum = len(inversions[key])
                    minimum_key = key

            calculated_results[(initial_s, final_s)] = inversions[minimum_key]

            return inversions[minimum_key]

# returns a set of tuples of neighbours
def find_neighbours(array):
    neighbours = set()
    for i in range(len(array)-1):
        neighbours.add((array[i], array[i+1]))
        neighbours.add((array[i+1], array[i]))

    return neighbours

def find_breaks(final, neighbours):
    breaks = []
    for i in range(len(final)-1):
        if (final[i], final[i+1]) not in neighbours:
            breaks.append((final[i], final[i+1]))

    return breaks

# reverses a sequence between two breaks
def reverse(seq, A, B):
    for i in range(len(seq)-1):
        if (seq[i], seq[i+1]) == A:
            for j in range(len(seq)-1):
                if (seq[j], seq[j+1]) == B:
                    return seq[:i+1] + seq[j:i:-1] + seq[j+1:]

# converts a list of numbers to character string
# 131 -> bdb
def string(seq):
    s = ""
    for item in seq:
        s += chr(ord('a') + item - 1)

    return s
    

main()