import unittest


class TestSolutionApril(unittest.TestCase):
    def testSolution(self):
        pass

    def testSol25Apr(self):
        from April2021.sol_25 import Solution
        inputs = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            (
                [[5, 1, 9, 11], [2, 4, 8, 10],
                 [13, 3, 6, 7], [15, 14, 12, 16]],  # inp
                [[15, 13, 2, 5], [14, 3, 4, 1],
                 [12, 6, 8, 9], [16, 7, 10, 11]]  # out
            ),
            ([[1]], [[1]])
        ]
        sol = Solution()
        for inp, out in inputs:
            sol.rotate(inp)
            self.assertEqual(out, inp)

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
        from April2021.sol28 import Solution, test_cases

        sol = Solution()
        for inp, out in test_cases:
            res = sol.uniquePathsWithObstacles(inp)
            self.assertEqual(out, res, inp)


if __name__ == '__main__':
    unittest.main()
