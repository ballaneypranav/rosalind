n = int(input())
permutation = [int(x) for x in input().split()]

decreasing = [[permutation[0]]]
increasing = [[permutation[0]]]

# longest increasing subsequence
for i in range(1, len(permutation)):
    
    max_length = 0
    sub_LIS_index = None
    # find all the LIS before i
    for j in range(0, i):
        # that end in a number smaller than permutation[i]
        if increasing[j][-1] < permutation[i]:
            # and store the index of the longest
            if len(increasing[j]) > max_length:
                max_length = len(increasing[j])
                sub_LIS_index = j
            
    if sub_LIS_index is None:
        increasing.append([permutation[i]])
    else:
        increasing.append(increasing[sub_LIS_index] + [permutation[i]])

# longest decreasing subsequence
for i in range(1, len(permutation)):
    
    max_length = 0
    sub_LIS_index = None
    # find all the LIS before i
    for j in range(0, i):
        # that end in a number smaller than permutation[i]
        if decreasing[j][-1] > permutation[i]:
            # and store the index of the longest
            if len(decreasing[j]) > max_length:
                max_length = len(decreasing[j])
                sub_LIS_index = j
            
    if sub_LIS_index is None:
        decreasing.append([permutation[i]])
    else:
        decreasing.append(decreasing[sub_LIS_index] + [permutation[i]])

longest_seq = []

max_length = 0
for seq in increasing:
    if len(seq) > max_length:
        max_length = len(seq)
        longest_seq = seq
print(*longest_seq)

max_length = 0
for seq in decreasing:
    if len(seq) > max_length:
        max_length = len(seq)
        longest_seq = seq
print(*longest_seq)