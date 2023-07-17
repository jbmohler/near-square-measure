import math


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


bin_count = 73
BINS = {i: [] for i in range(bin_count + 2)}


def bin(N, sf):
    global bin_count, BINS

    for i in range(bin_count + 2):
        if sf <= (i / bin_count):
            BINS[i].append(N)
            break


def dist():
    for N in range(1, 100_000):
        sf = square_factor(N)

        bin(N, sf)


if __name__ == "__main__":
    dist()

    for i in range(bin_count + 2):
        if i > bin_count and len(BINS[i]) == 0:
            continue
        print(f"{i/bin_count:6.4f}:  {len(BINS[i]):5n} {str(BINS[i])[:150]}")
