import math
import random


def square_factor(n):
    """
    >>> .999<square_factor(25)<=1.
    True
    >>> .7<square_factor(30)<.999
    True
    >>> .01<square_factor(34)<.3
    True
    >>> 0.<=square_factor(17)<.01
    True
    """

    assert isinstance(n, int) and n >= 1

    sq = math.sqrt(n)
    sq = int(sq)

    if sq**2 == n:
        # special case is especially import for n=1 since that would result in
        # division log(1) / log(1).
        return 1.0

    while sq >= 1:
        large_fac = n // sq

        if sq * large_fac == n:
            return math.log(sq) / math.log(large_fac)

        sq -= 1

    raise NotImplementedError("should not get here")


def sums():
    ssf = 0
    next_print = random.randrange(990, 1010)
    for N in range(1, 1000):
        sf = square_factor(N)
        ssf += sf
        if N == next_print:
            next_print += random.randrange(990, 1010)
            print(
                f"\u03c8({N:5})={ssf:7.2f} (ratio {ssf/N:5.3f}) (increment {sf:8.5f})"
            )


if __name__ == "__main__":
    sums()
