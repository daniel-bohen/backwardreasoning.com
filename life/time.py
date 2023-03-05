import pandas as pd 
import numpy as np 
import datetime as dt


def temporal_span(start_date: dt.datetime, end_date: dt.datetime, dependent: str, time_unit: str) -> pd.DataFrame:
    """Create a dataframe where one column is a time span and the other is a dependent variable
    
    Parameters
    ----------
    start_date : datetime.datetime
        The start date of the time span
    end_date : datetime.datetime
        The end date of the time span
    dependent : str
        The name of the dependent variable
    time_unit : str
        The time unit of the time span. Must be one of 'minute', 'hour', 'day', 'week', 'month', 'year'

    Returns
    -------
    empty_span : pd.DataFrame
        A dataframe with a time span and a dependent variable

    """

    # Create a list of dates
    dates = pd.date_range(start_date, end_date, freq=time_unit)

    # Create a dataframe with the dates
    empty_span = pd.DataFrame(dates, columns=['time_span'])

    # Create a column for the dependent variable
    empty_span[dependent] = np.nan

    return empty_span


def add_habit():

if __name__ == "__main__":
    # Create a time span
    time_span = temporal_span(dt.datetime(2021, 1, 1), dt.datetime(2021, 1, 31), 'dependent', 'D')

    # Print the time span
    print(time_span)

