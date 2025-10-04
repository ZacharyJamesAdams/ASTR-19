'''prompt5
Write a Python program that writes out a table of the function sin(x) vs. x,
where x is tabulated between 0 and 2pi with a thousand entries. Follow the basic
Python program structure, including a main program function.
'''

import numpy as np


def get_sin_data(start, stop, num):
    X = np.linspace(start, stop, num, endpoint=False)
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
    x, y = get_sin_data(0, np.pi*2, 1000)
    table = tabulate(x, y)
    print(table)


if __name__ == '__main__':
    main()
