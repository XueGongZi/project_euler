import unittest as ut
import sys
import poisson_distribution_i as pd
class TestSum(ut.TestCase):
    def test_poisson_distribution(self):
        ans = 0.067
        self.assertEqual(round(pd.Solution().poisson_distribution_equal_k_and_average(5, 2.5), 3), ans, "equal to 0.067")

if __name__ == "__main__":
    ut.main()
