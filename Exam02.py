# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260425

import math
from fractions import Fraction


def mapFunctionQ2(L: list[int])-> list[Fraction]:
    # if len(L) % 2 == 0: # even or odd
    #     for i in range(1,len(L),2):
    #         print(Fraction(sum(L[i:]),i)) # 1,3,5
    #     return [2]
    # else:
    #     for i in range(1,len(L)-1,2):
    #         print(Fraction(sum(L[i:]),i)) # 1,3,5
    #     return [1]
    return [Fraction(sum(L[i:]),i) for i in range(1,len(L),2)] if len(L) % 2 == 0 else [Fraction(sum(L[i:]),i) for i in range(1,len(L)-1,2)]


if __name__ == "__main__":
    print(Fraction(1, 3))
    print("example:")
    print(mapFunctionQ2([1,2,3,4,5,6]))
    print()
    print(mapFunctionQ2([1, 2, 3, 4, 5, 6,7]))