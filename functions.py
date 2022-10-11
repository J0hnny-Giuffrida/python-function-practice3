def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(max_num(4, 5, 7))
# -----------------------------------------


list = [8, 10, 'cat', 'dog']


def mult_list(list, multiplier):
    for i in range(len(list)):
        if type(list[i]) == int:
            list[i] = list[i] * multiplier


mult_list(list, 4)
print(list)
# --------------------------------------------


def rev_string(string_arg):
    reversed_string = ''
    for i in reversed(string_arg):
        reversed_string += i
    print(reversed_string)


rev_string('hero')
# ----------------------------------------------


def num_within(num, start_range, end_range):
    if type(num) != int:
        print('Argument must be an integer')
    elif num >= start_range and num <= end_range:
        return True
    else:
        return False


print(num_within(4, 2, 10))
# ------------------------------------------------


pyramid = [[1], [1, 1]]


def pascal(n):
    if n < 1:
        print('Number of rows must be greater than 0')
    elif n == 1:
        print(pyramid[0])
    else:
        row_number = 2
        while len(pyramid) < n:
            row = []
            row_prev = pyramid[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(pyramid[row_number - 1]
                               [i - 1] + pyramid[row_number-1][i])
                else:
                    row.append(1)
            pyramid.append(row)
            row_number += 1
        for row in pyramid:
            print(row)


pascal(7)
