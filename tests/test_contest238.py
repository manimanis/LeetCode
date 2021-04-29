import unittest
import io
import sys


class TestContest238(unittest.TestCase):
    def testProblem2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        from contests.contest238_p2 import Solution, test_cases        
        sol = Solution()
        for inp, out in test_cases:
            outcome = sol.maxFrequency(*inp)
            self.assertEqual(out, outcome)

    def testProblem5(self):
        from contests.contest238_p5 import Solution, test_cases
        sol = Solution()
        for inp, out in test_cases:
            outcome = sol.maxBuilding(*inp)
            self.assertEqual(out, outcome)

