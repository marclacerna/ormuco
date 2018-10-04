from unittest import TestCase
from question_b import CheckInputs


class TestCheckInputs(TestCase):
    def test_compare_greater(self):
        str1 = '4.5'
        str2 = '2'
        test = CheckInputs(str1, str2)

        self.assertEqual(test.compare(), '4.5 greater than 2.0')

    def test_compare_less(self):
        str1 = '2'
        str2 = '4.5'
        test = CheckInputs(str1, str2)

        self.assertEqual(test.compare(), '2.0 less than 4.5')

    def test_compare_equal(self):
        str1 = '4.5'
        str2 = '4.5'

        test = CheckInputs(str1, str2)

        self.assertEqual(test.compare(), '4.5 is equal 4.5')

