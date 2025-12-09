
# def hanoi(n, start, aux, end):
#     if n==1:
#         print(f"hanoi : ({start}) -> ({end})")
#     else:
#         hanoi(n-1, start, aux, end)
#         print(f"hanoi : ({start}) -> ({end})")
#         hanoi(n-1, aux, start, end)
#         return
#
#
# hanoi(4,"A","C","B")

def slowo(sl):
    if len(sl) <= 1:
        return sl
    return slowo(sl[1:]) + sl[0]

print(slowo("kot"))
