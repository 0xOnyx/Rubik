import sys
import numpy as np

class RubikCube:
    def __init__(self):
        self.cube = np.zeros((6, 3, 3), dtype=int)
        for i in range(6):
            self.cube[i] = np.full((3, 3), i)

    def rotate(self, face, direction):


def main(argv, argc):
    if argc < 2:
        print("Usage: rubik.py \"spin sequences\"")
        return
    sequence = argv[1].split()
    print(sequence)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv, len(sys.argv))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
