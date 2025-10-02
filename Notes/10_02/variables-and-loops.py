import numpy as np

def main():
    i,n, x = 0, 10, 19.0

    y = np.zeros(n, dtype=float)

    for i in range(n):
        y[i] = 2.0 * i + 1.0
    
    for val in y:
        print(val)


if __name__ == "__main__":
    main()