S1 = [float(x) for x in input().split()]
S2 = [float(x) for x in input().split()]

MD = {}
for s1 in S1:
    for s2 in S2:
        diff = round(s1-s2, 5)
        if diff in MD.keys():
            MD[diff] += 1
        else:
            MD[diff] = 1
        # print(s1, s2, diff)

max = 0
difference = 0
for diff in MD:
    if MD[diff] > max:
        max = MD[diff]
        difference = diff

print(max)
print(difference)