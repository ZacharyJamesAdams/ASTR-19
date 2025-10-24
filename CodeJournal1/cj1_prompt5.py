# This program produces a table x vs. sin(x) given an iterable of
#   x-values from 0 to 2pi (exclusive).
# Functions:
#   get_data:
#     returns a list of x values and a list of sin(x) values
#   tabulate:
#     returns a string containing the formatted table of the two input lists

import numpy as np


def get_data(x_start, x_stop, sample_count):
    X = np.linspace(x_start, x_stop, sample_count, endpoint=False)
    Y = np.sin(X)
    return X, Y


def tabulate(X, Y):
    format_string = '|  {0:<{2}}  |  {1:<{3}}  |'
    x_width = max((len(str(i)) for i in X))
    y_width = max((len(str(i)) for i in Y))
    header = '|  {0:^{2}}  |  {1:^{3}}  |'.format(
        'x', 'sin(x)', x_width, y_width)
    h_div = '|' + '-' * (len(header)-2) + '|'
    table = [header, h_div]
    for x, y in zip(X, Y):
        table.append(format_string.format(x, y, x_width, y_width))
    return '\n'.join(table)


def main():
    x, y = get_data(0, np.pi*2, 1000)
    table = tabulate(x, y)
    print(table)


if __name__ == '__main__':
    main()
