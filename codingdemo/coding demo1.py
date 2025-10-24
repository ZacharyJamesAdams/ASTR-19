import sys
import numpy as np

def main():
    x = 0.0
    for i in range(20):
        x = 2.0*float(i) + float(19)
        print(f'The value of x = {x}')

if __name__ == '__main__':
    main()