import unittest
import pytest
import pandas as pd


class TestDataSummary(unittest.TestCase):
    def setUp(self):
        # test DataFrame
        df1_data = [[1, 'a'], [2, 'b'], [3, 'c']]
        df1_cols = ['numbers', 'letters']
        self.df1 = pd.DataFrame(data=df1_data, columns=df1_cols)
        # for shape
        self.sh_idx = ['Number of rows', 'Number of columns']
        self.sh_data = [[3], [2]]
        # for types freq
        self.freq_idx = ['int64', 'object']
        self.freq_data = [[1], [1]]
        # for summary
        self.sum_col = ['Values']
        self.sum_idx = ['Number of rows', 'Number of columns', 'int64', 'object']
        self.sum_data = [[3], [2], [1], [1]]

    @pytest.fixture(autouse=True)
    def _pass_fixture(self, capsys):
        self.capsys = capsys

    def test_shape(self):
        expected = pd.DataFrame(data=self.sh_data, columns=self.sum_col, index=self.sh_idx)
        row, col = self.df1.shape
        result = pd.DataFrame(data=[[row], [col]], columns=self.sum_col, index=self.sh_idx)
        self.assertTrue(result.equals(expected))

    def test_type_freq(self):
        expected = pd.DataFrame(data=self.freq_data, columns=self.sum_col, index=self.freq_idx)
        counter, types = {}, self.df1.dtypes
        for dtype in types:
            tmp = str(dtype)
            if tmp in counter.keys():
                counter[tmp] += 1
            else:
                counter[tmp] = 1
        values, idx = [[value] for value in counter.values()], list(counter.keys())
        result = pd.DataFrame(data=values, columns=self.sum_col, index=idx)
        self.assertTrue(result.equals(expected))

    def test_data_summary(self):
        # test the final dataframe
        expected_df = pd.DataFrame(data=self.sum_data, columns=self.sum_col, index=self.sum_idx)
        data1, data2 = [[3], [2]], [[1], [1]]
        df_shape = pd.DataFrame(data=data1, columns=self.sum_col, index=self.sh_idx)
        df_freqs = pd.DataFrame(data=data2, columns=self.sum_col, index=self.freq_idx)
        result_df = pd.concat([df_shape, df_freqs])
        self.assertTrue(expected_df.equals(result_df))
        # test the output
        message = '--- Data summary ---'
        print(message, result_df, sep='\n')
        result_stdout = self.capsys.readouterr()
        print(message, expected_df, sep='\n')
        expected_stdout = self.capsys.readouterr()
        self.assertEqual(expected_stdout, result_stdout)


if __name__ == '__main__':
    unittest.main()
