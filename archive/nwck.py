import random
from re import L
import string
from sys import setrecursionlimit
setrecursionlimit(10000)


def main():
    with open('rosalind_nwck.txt', 'r') as f:
        lines = f.readlines()

    tree_strings = []
    queries = []

    for i in range(0, len(lines), 3):
        lines[i] = lines[i].strip()
        if lines[i] == '':
            continue

        tree_strings.append(lines[i])
        x, y = lines[i+1].strip().split()
        queries.append((x, y))

    for i in range(len(tree_strings)):
        tree_tokens = tokenize(tree_strings[i])

        x, y = queries[i]
        root_to_x = path_from_root(x, tree_tokens)
        root_to_y = path_from_root(y, tree_tokens)

        i = 0
        while i < min(len(root_to_x), len(root_to_y)) and root_to_x[i] == root_to_y[i]:
            i += 1
        print(len(root_to_x) + len(root_to_y) - 2*i, end=" ")

def path_from_root(node, tree_tokens):

    if tree_tokens == []:
        return []

    # if this is a top level node:  (...)x
    # it must be balaneced
    # and the stuff within the brackets must also be balanced
    # because if it is of the form "(...)x, (...)y"
    # then "(...)x, (...)y" is balanced but "...)x, (..." is not
    if len(tree_tokens) > 3 and \
            tree_tokens[0] == '(' and \
            tree_tokens[-2] == ')' and \
            balanced(tree_tokens) and \
            balanced(tree_tokens[1:-2]):

        root = tree_tokens[-1]
        if node == root:
            return [root]
        else:
            return [root] + path_from_root(node, tree_tokens[1:-2])
    # else the tree_tokens consists of comma separated values, 
    # like A, B, (C, D), E
    # in which, all these could be called top level nodes at this point
    subtrees = [[]]
    k = 0
    for token in tree_tokens:
        if subtrees[k] != [] and balanced(subtrees[k]):
            if token in ',':
                subtrees.append([])
                k += 1
                continue
            elif token not in '();':
                subtrees[k].append(token)
                subtrees.append([])
                k += 1
                continue
        elif subtrees[k] == [] and token == ',':
            continue

        subtrees[k].append(token)

    for subtree in subtrees:
        if subtree == [node]:
            return subtree
        elif node in subtree:
            return path_from_root(node, subtree)
            

def tokenize(tree_string):
    tokens = []
    node = ""
    for c in tree_string:
        if c in ['(', ',', ')', ';']:
            if node != '':
                tokens.append(node)
                node = ''
            tokens.append(c)
        elif c == ' ':
            continue
        else:
            node += c
    if node != '':
        tokens.append(node)
    
    tokens_filled = []

    for i in range(len(tokens)-1):
        tokens_filled.append(tokens[i])
        if tokens[i] + tokens[i+1] in [',,', '),', '))', ',)', ');']:
            res = 'aa'
            while res in tokens or res in tokens_filled:
                res = ''.join(random.choices(string.ascii_letters, k=2))
            tokens_filled.append(res)
    if tokens[-1] != ';':
        tokens_filled.append(tokens[-1])

    return tokens_filled

def balanced(tree_tokens):
    open_brackets = 0
    for token in tree_tokens:
        if open_brackets == 0:
            if token == '(':
                open_brackets += 1
            elif token == ')':
                return False
        else:
            if token == '(':
                open_brackets += 1
            elif token == ')':
                open_brackets -= 1
    
    return open_brackets == 0

main()