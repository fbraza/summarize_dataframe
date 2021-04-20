import unittest
import pytest
import pandas as pd
from summarize_dataframe.summarize_df import data_summary, display_summary


class TestDataSummary(unittest.TestCase):
    def setUp(self):
        # initialize dataframe to test
        df_data = [[1, 'a'], [2, 'b'], [3, 'c']]
        df_cols = ['numbers', 'letters']
        self.df = pd.DataFrame(data=df_data, columns=df_cols)
        # initialize expected dataframe
        exp_col = ['Values']
        exp_idx = ['Number of rows', 'Number of columns', 'int64', 'object']
        exp_data = [[3], [2], [1], [1]]
        self.exp_df = pd.DataFrame(data=exp_data, columns=exp_col, index=exp_idx)

    @pytest.fixture(autouse=True)
    def _pass_fixture(self, capsys):
        self.capsys = capsys

    def test_data_summary(self):
        expected_df = self.exp_df
        result_df = data_summary(self.df)
        self.assertTrue(expected_df.equals(result_df))

    def test_display(self):
        print('---- Data summary ----', self.exp_df, sep='\n')
        expected_stdout = self.capsys.readouterr()
        display_summary(self.df)
        result_stdout = self.capsys.readouterr()
        self.assertEqual(expected_stdout, result_stdout)


if __name__ == '__main__':
    unittest.main()
