class CheckInputs:

    def __init__(self, input1, input2):
        try:
            self.input1 = float(input1)
            self.input2 = float(input2)
        except ValueError:
            print('Both inputs must be a number')

    def compare(self):
        if self.input1 > self.input2:
            return '{} greater than {}'.format(self.input1, self.input2)

        elif self.input1 == self.input2:
            return '{} is equal {}'.format(self.input1, self.input2)

        else:
            return '{} less than {}'.format(self.input1, self.input2)