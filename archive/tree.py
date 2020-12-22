with open('rosalind_tree.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0].strip())

nodes = list(range(1, n+1))

connected_components = []

for line in lines[1:]:
    x, y = tuple([int(x) for x in line.strip().split()])
    if x in nodes and y in nodes:
        connected_components.append(set([x, y]))
        nodes.remove(x)
        nodes.remove(y)
    elif x in nodes:
        for component in connected_components:
            if y in component:
                component.add(x)
                nodes.remove(x)
    elif y in nodes:
        for component in connected_components:
            if x in component:
                component.add(y)
                nodes.remove(y)
    else:
        c1 = set()
        c2 = set()
        for component in connected_components:
            if x in component:
                c1 = component
            if y in component:
                c2 = component
        c1.update(c2)
        connected_components.remove(c2)

for node in nodes:
    connected_components.append(set([node]))

print(len(connected_components) - 1)

