import sys

class Shape:
    def __init__(self, nsides=3, length=1.):
        self.nsides = nsides
        self.side_length = length
        self.perimeter = nsides * length

    def print(self):
        print('Here is our shape!')
        print(f'Number of sides = {self.nsides}')
        print(f'Length of sides = {self.side_length}')
        print(f'The perimeter of this shape = {self.perimeter}')

def main():
    nsides = 3
    length = 10.
    
    if len(sys.argv) >= 2:
        nsides = int(sys.argv[1])
    if len(sys.argv) >= 3:
        length = float(sys.argv[2])

    s = Shape(nsides,length)    
    s.print()

if __name__ == '__main__':
    main()