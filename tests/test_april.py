import unittest


class TestSolutionApril(unittest.TestCase):
    def testSolution(self):
        pass

    def testSol25Apr(self):
        from April2021.sol_25 import Solution, test_cases
        sol = Solution()
        for inp, out in test_cases:
            sol.rotate(*inp)
            self.assertEqual(out, inp[0])

    def testSol26Apr(self):
        from April2021.sol_26_slow import Solution as Solution1
        from April2021.sol_26_fast import Solution as Solution2, test_cases

        sol = Solution1()
        for inp, out in test_cases:
            res = sol.furthestBuilding(*inp)
            self.assertEqual(out, res)

        sol = Solution2()
        for inp, out in test_cases:
            res = sol.furthestBuilding(*inp)
            self.assertEqual(out, res)

    def testSol28Apr(self):
        from April2021.sol_28 import Solution, test_cases

        sol = Solution()
        for inp, out in test_cases:
            res = sol.uniquePathsWithObstacles(*inp)
            self.assertEqual(out, res, inp)

    def testSol27Apr(self):
        from April2021.sol_27 import Solution, test_cases

        sol = Solution()
        for inp, out in test_cases:
            res = sol.isPowerOfThree(*inp)
            self.assertEqual(out, res, inp)

    def testSol29Apr(self):
        from April2021.sol_29 import Solution, test_cases

        sol = Solution()
        for inp, out in test_cases:
            res = sol.searchRange(*inp)
            self.assertEqual(out, res, inp)

if __name__ == '__main__':
    unittest.main()
