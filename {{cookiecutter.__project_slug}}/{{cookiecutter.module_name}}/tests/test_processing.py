import unittest
from pandas import DataFrame
from pandas.testing import assert_frame_equal

from {{cookiecutter.module_name}}.processing import filter_outliers


class TestFilterOutliers(unittest.TestCase):
    def setUp(self):
        self.data = DataFrame({
            'A': [10, 20, 30, 40, 50],
            'B': [5, 15, 25, 35, 45]
        })

    def test_filter_outliers_column_A_threshold_35(self):
        filtered_df = filter_outliers(self.data, 'A', 35)
        expected_df = DataFrame({
            'A': [10, 20, 30],
            'B': [5, 15, 25]
        })
        assert_frame_equal(filtered_df, expected_df)

    def test_filter_outliers_column_B_threshold_10(self):
        filtered_df = filter_outliers(self.data, 'B', 10)
        expected_df = DataFrame({
            'A': [10],
            'B': [5]
        })
        print('DF:')
        print(filtered_df.to_markdown())
        print(expected_df.to_markdown())
        assert_frame_equal(filtered_df, expected_df)

    def test_filter_outliers_column_A_threshold_0(self):
        filtered_df = filter_outliers(self.data, 'A', 5)
        self.assertTrue(filtered_df.empty)

    def test_filter_outliers_empty_dataframe(self):
        empty_df = DataFrame({'A': []})
        filtered_df = filter_outliers(empty_df, 'A', 10)
        expected_df = DataFrame({'A': []})
        assert_frame_equal(filtered_df, expected_df)

    def test_filter_outliers_nonexistent_column(self):
        with self.assertRaises(KeyError):
            filter_outliers(self.data, 'NonExistentColumn', 10)

    def test_filter_outliers_negative_threshold(self):
        filtered_df = filter_outliers(self.data, 'A', -10)
        self.assertTrue(filtered_df.empty)
