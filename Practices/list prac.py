# n = 10
# l = [0, 8, 8, 5, 8, 8, 8, 7, 9, 5]
# l.sort()
# l.reverse()
# print(l)
# max1 = max(l)
# l.remove(max(l))
# print(l)
#
# while n:
#     if max(l) == max1:
#         l.remove(max1)
#         n += 1
#     else:
#         print(l[0])
#         exit()


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(type(arr[0]))
    # arr.sort()
    # arr.reverse()
    # max1 = max(arr)
    # arr.remove(max(arr))
    #
    # while n:
    #     if max(arr) == max1:
    #         arr.remove(max1)
    #         n += 1
    #
    #     else:
    #         print(arr[0])
    #         exit()