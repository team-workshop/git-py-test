import unittest
import numpy as np


class TestEEGQuality(unittest.TestCase):

    def setUp(self):
        """
        Prepare the test fixture
        :return:
        """
        pass

    def tearDown(self):
        """
        Reset test fixture
        :return:
        """
        pass

    def test_compute_quality_index_returns_array(self):
        """
        Assess that compute_quality_index output type is array
        :return:
        """
        self.assertIsInstance(np.asarray([]), np.ndarray,
                              "The test should always pass.")

        # Todo: modify this test to test compute_quality_index output
        self.assertIsInstance("this is a string", np.ndarray,
                              "The object is not of type array")

    def test_compute_quality_index_returns_numerical_values(self):
        """
        Assess that compute_quality_index array values are numerical
        :return:
        """
        arr = [0., 1., 3.]
        for el in arr:
            self.assertIsInstance(el, float, "This test should always pass")

        # Todo: modify this test to test compute_quality_index output
        arr_with_string = [0., 1., "this is a string"]
        for el in arr_with_string:
            self.assertIsInstance(el, float,
                                  "One el in arr_with_string is not a float")

    # Todo: could you think of more checks to do? What is the best case
    # scenario for the input? Worst case scenario?
    # Any checks additional checks to add for the parameters of the function?
    # Shall we refactor the function?
