# This program defines a function that takes the
# argument, x, and returns the value of x^3 + 8.
# Additionally, the main loop prints the returned value
# and, if that value is higher than 27, prints 'YAY!' 

def f(x):
    return x**3 + 8

def main():
    x = 9
    func = f
    result = func(x)
    print(f'{func.__name__}({x}) = {f(x)}')
    if result > 27:
        print('YAY!')

if __name__ == '__main__':
    main()
    