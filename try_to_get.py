import itertools
import re
stuff = "tapssjpaguwt"

for subset in itertools.permutations(stuff, len(stuff)):
    s = ''.join(subset)

    print s
