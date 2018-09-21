import argparse

#  1
# 2 3
#  4
# 5 6
#  7

NUM_LCD_MAP = {
    '0': (1, 2, 3, 5, 6, 7),
    '1': (3, 6),
    '2': (1, 3, 4, 5, 7),
    '3': (1, 3, 4, 6, 7),
    '4': (2, 3, 4, 6),
    '5': (1, 2, 4, 6, 7),
    '6': (1, 2, 4, 5, 6, 7),
    '7': (1, 3, 6),
    '8': (1, 2, 3, 4, 5, 6, 7),
    '9': (1, 2, 3, 4, 6),
}


class LcdPrinter(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def print_number(self, number):
        for line in range(2*self.height + 1):
            self.print_line(number, line)
            print('')

    def print_line(self, number, line):
        for digit in number:
            if line == 0:
                side_char = ' '
                center_char = '_' if 1 in NUM_LCD_MAP[digit] else ' '
                self.print_digit_line(side_char, center_char, side_char)
            elif 0 < line <= self.height:
                left_char = '|' if 2 in NUM_LCD_MAP[digit] else ' '
                right_char = '|' if 3 in NUM_LCD_MAP[digit] else ' '
                center_char = '_' if 4 in NUM_LCD_MAP[digit] else ' '
                if line == self.height:
                    self.print_digit_line(left_char, center_char, right_char)
                else:
                    self.print_digit_line(left_char, ' ', right_char)
            else:
                left_char = '|' if 5 in NUM_LCD_MAP[digit] else ' '
                right_char = '|' if 6 in NUM_LCD_MAP[digit] else ' '
                center_char = '_' if 7 in NUM_LCD_MAP[digit] else ' '
                if line == 2 * self.height:
                    self.print_digit_line(left_char, center_char, right_char)
                else:
                    self.print_digit_line(left_char, ' ', right_char)

    def print_digit_line(self, left_char, center_char, right_char):
        print(left_char, end='')
        for _ in range(self.width):
            print(center_char, end='')
        print(right_char, end='')


def main():
    parser = argparse.ArgumentParser(description='Print numbers like on a LCD display.')
    parser.add_argument('number', type=str)
    parser.add_argument('--height', type=int, required=False, default=1)
    parser.add_argument('--width', type=int, required=False, default=1)
    args = parser.parse_args()

    printer = LcdPrinter(args.height, args.width)
    printer.print_number(args.number)


if __name__ == "__main__":
    main()
