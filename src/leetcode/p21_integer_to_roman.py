# def turn_integer_to_roman(input):
#     values = [1000, 900 , 500, 400 , 100, 90  , 50 , 40  , 10 , 9   , 5  , 4   , 1]
#     symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#     i = 0
#     result = ""
#     while i < len(values):
#         while input >= values[i]:
#             input -= values[i]
#             result += symbols[i]
#
#         i += 1
#     return result


def turn_integer_to_roman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ""

    for i in range(len(values)):
        while num >= values[i]:
            num -= values[i]
            result += symbols[i]

    return result


if __name__ == '__main__':  # input是內建函數  這是關鍵字不能用
       # num = 46; # XLVI
       # num = 954; # CMLIV
       # num = 10; # X
       # num = 60; # LX
    num = 61 # LXI
    # num = 100; # C
#     num = 3749; # MMMDCCXLIX
    result = turn_integer_to_roman(num)
    print(result)

#
# Runtime
# 56
# ms
# Beats
# 16.88%
# Analyze Complexity
# Memory
# 16.46
# MB
# Beats
# 81.69%
