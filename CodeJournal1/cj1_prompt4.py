# This program defines an Animal class that stores descriptive data about an animal
# and provides a method to print a human-description to the terminal.

class Animal():
    def __init__(self,
                 arm_length: float,
                 leg_length: float,
                 eye_count: int,
                 has_tail: bool,
                 has_fur: bool):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.eye_count = int(eye_count)
        self.has_tail = bool(has_tail)
        self.has_fur = bool(has_fur)

    def describe(self):
        description = \
            f'This animal\'s arms are {self.arm_length} meters long, and its legs are {self.leg_length} meters long.\n' \
            f'It is known to have {self.eye_count} eye{"s" if self.eye_count != 1 else ''} and {'a' if self.has_tail else 'no'} tail.\n' \
            f'It is{" covered in fur" if self.has_fur else ", sadly, bald."}'
        print(description)


def main():
    bison = Animal(2,3,2,True,True)
    bison.describe()

if __name__ == "__main__":
    main()