class CheckLines:

    def __init__(self):
        self.line1 = None
        self.line2 = None
        self.overlaps = False

    def set_lines(self):
        """
        Gets line1 and line2 values
        """
        self.line1 = [int(i) for i in str(input('enter first line: ')).rstrip().split(' ')]
        self.line2 = [int(i) for i in str(input('enter second line: ')).rstrip().split(' ')]

    def get_lines(self):
        print("Lines {} and {} {}".format(self.line1, self.line2,
                                          "overlaps" if a.do_lines_overlap() else "does not overlap"))

    def do_lines_overlap(self):
        """Checks if line1 and line2 overlaps
        return: returns true is line1 and line2 overlaps
        """
        for i in self.line1:
            if i in range(self.line2[0] , self.line2[1]):
                self.overlaps = True

        return self.overlaps


if __name__ == "__main__":
    a = CheckLines()
    a.set_lines()
    a.get_lines()
