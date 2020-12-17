# https://aliquote.org/post/rosalind-independent-alleles

from scipy.special import binom

def foo(k, N):
    def p(n, k):
        return binom(2**k, n) * 0.25**n * 0.75**(2**k - n)
    return 1 - sum(p(n, k) for n in range(N))

k, n = tuple([int(x) for x in input().split()])
print(foo(k, n))