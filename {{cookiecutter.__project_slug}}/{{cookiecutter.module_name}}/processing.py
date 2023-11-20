from pandas import DataFrame


def filter_outliers(data: DataFrame,
                    column_to_filter: str,
                    threshold: int) -> DataFrame:
    '''
    Filters out all rows from data which have a value larger
    than the threshold.
      Parameters:
        data (DataFrame): Dataframe to filter
        column_to_filter (str): Name of the column you want to filter on
        threshold (int): Threshold value to filter on. Values larger than
        the threshold are removed
      Returns:
        filtered_df (DataFrame): Dataframe containing the filtered rows
    '''
    filtered_df = data[data[column_to_filter] <= threshold]
    return filtered_df
