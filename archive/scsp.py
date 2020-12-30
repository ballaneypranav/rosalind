def main():
    a = input()
    b = input()

    print(interleave(a, b))

archive = {}

def interleave(a, b):

    if (a, b) in archive.keys():
        return archive[(a, b)]
    elif len(a) <= 1 or len(b) <= 1:
        result = a + b
        archive[(a, b)] = result
        return result
    elif a[0] == b[0]:
        result = a[0] + interleave(a[1:], b[1:])
        archive[(a, b)] = result
        return result
    else:
        x = a[0] + interleave(a[1:], b)
        y = b[0] + interleave(a, b[1:])

        if len(x) < len(y):
            archive[(a, b)] = x
            return x
        else:
            archive[(a, b)] = y
            return y

main()

