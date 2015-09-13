# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".

import unittest

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0 or denominator == 0:
            return '0'

        if numerator^denominator  < 0:
            sign = '-'
        else:
            sign = ''

        numerator = abs(numerator)
        denominator = abs(denominator)

        q = numerator/denominator        
        r = numerator%denominator
        r_dict = dict()

        s1 = str(q)
        s2 = ''

        if r > 0:
            s1 += '.'
            r_dict[r] = 0

        pos = 0
        while r != 0:
            numerator = r*10
            q = numerator/denominator
            next_r = abs(numerator%denominator)

            s2 += str(q)

            try:
                pre_pos = r_dict[next_r]
                s2 = s2[:pre_pos] + '(' + s2[pre_pos:] + ')'
                r = 0
                break
            except KeyError:
                # this remainder is not met before
                pos += 1
                r_dict[next_r] = pos 
                
                r = next_r
                
        return sign + s1 + s2

        

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case0(self):
        numerator = 1
        denominator = 2
        self.assertEqual("0.5", self.solution.fractionToDecimal(numerator, denominator))

    def test_case1(self):
        numerator = 2
        denominator = 1
        self.assertEqual("2", self.solution.fractionToDecimal(numerator, denominator))

    def test_case2(self):
        numerator = 2
        denominator = 3
        self.assertEqual("0.(6)", self.solution.fractionToDecimal(numerator, denominator))

    def test_case3(self):
        numerator = 5
        denominator = 4
        self.assertEqual("1.25", self.solution.fractionToDecimal(numerator, denominator))

    def test_case4(self):
        numerator = 8
        denominator = 3
        self.assertEqual("2.(6)", self.solution.fractionToDecimal(numerator, denominator))

    def test_case5(self):
        numerator = 11
        denominator = 4
        self.assertEqual("2.75", self.solution.fractionToDecimal(numerator, denominator))

    def test_case6(self):
        numerator = 0
        denominator = 0
        self.assertEqual("0", self.solution.fractionToDecimal(numerator, denominator))

    def test_case7(self):
        numerator = 1
        denominator = 99
        self.assertEqual("0.(01)", self.solution.fractionToDecimal(numerator, denominator))

    def test_case8(self):
        numerator = 1
        denominator = 6
        self.assertEqual("0.1(6)", self.solution.fractionToDecimal(numerator, denominator))
          
if __name__ == '__main__':
    unittest.main() 
    # suite = unittest.TestSuite()
    # suite.addTest(MyTestCase("test_case26"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)