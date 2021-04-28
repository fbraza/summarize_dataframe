"""Get row and column count and dtype frequency

This modules provides an interface to output
some metadata about pandas DataFrame. it notably
output the number of rows and columns and the frequency
of each data type present in the DataFrame

"""

import pandas as pd


def data_summary(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Function defined to output details about the number
    of rows and columns and the column dtype frequency of
    the passed pandas DataFrame
    """

    def _shape(input_df: pd.DataFrame) -> pd.DataFrame:
        """
        Function defined to return a dataframe with details about
        the number of row and columns
        """
        row, col = input_df.shape
        return pd.DataFrame(
            data=[[row], [col]],
            columns=["Values"],
            index=["Number of rows", "Number of columns"],
        )

    def _dtypes_freq(input_df: pd.DataFrame) -> pd.DataFrame:
        """
        Function defined to return a dataframe with details about
        the pandas dtypes frequency
        """
        counter, types = {}, input_df.dtypes
        for dtype in types:
            tmp = str(dtype)
            if tmp in counter.keys():
                counter[tmp] += 1
            else:
                counter[tmp] = 1
        values = [[value] for value in counter.values()]
        index = list(counter.keys())
        return pd.DataFrame(data=values, columns=["Values"], index=index)

    result = pd.concat([_shape(input_df), _dtypes_freq(input_df)])
    return result


def display_summary(input_df: pd.DataFrame) -> None:
    """
    Function define to print out the result of the data summary
    """
    result = data_summary(input_df)
    message = "---- Data summary ----"
    print(message, result, sep="\n")
