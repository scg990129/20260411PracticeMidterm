# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260411


def mapFunction4Q2(L: list[int|float])-> list[int|float]:
    # result = []
    # for i in range(len(L)):
    #     print(sum(L[i:]))

    return [sum(L[i:]) for i in range(len(L))]

if __name__ == "__main__":
    print(mapFunction4Q2([1, 2, 3, 4]))