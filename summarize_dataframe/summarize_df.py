import pandas as pd


def data_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function defined to output details about the number
    of rows and columns and the column dtype frequency of
    the passed pandas DataFrame
    """
    def _shape(df: pd.DataFrame) -> pd.DataFrame:
        """
        Function defined to return a dataframe with details about
        the number of row and columns
        """
        row, col = df.shape
        return pd.DataFrame(data=[[row], [col]], columns=['Values'], index=['Number of rows', 'Number of columns'])

    def _dtypes_freq(df: pd.DataFrame) -> pd.DataFrame:
        """
        Function defined to return a dataframe with details about
        the pandas dtypes frequency
        """
        counter, types = {}, df.dtypes
        for dtype in types:
            tmp = str(dtype)
            if tmp in counter.keys():
                counter[tmp] += 1
            else:
                counter[tmp] = 1
        values = [[value] for value in counter.values()]
        return pd.DataFrame(data=values, columns=['Values'], index=list(counter.keys()))
    result_df = pd.concat([_shape(df), _dtypes_freq(df)])
    return result_df


def display_summary(df: pd.DataFrame) -> None:
    result_df = data_summary(df)
    message = '---- Data summary ----'
    print(message, result_df, sep='\n')
