import os

import pandas as pd
import datetime as dt

REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(REPO_PATH, "data/")


def dict_to_series(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Converts a DataFrame column with a dictionary to pandas series, where the column name is the
    dictionary key. The created pandas series is then concatenated to 'df'.

    Args:
        df: DataFrame containing dictionary
        column: Column in DataFrame that contains the dictionary
    """
    df = pd.concat([df, df[column].apply(pd.Series)], axis=1)
    df = df.drop(column, axis=1)

    return df


def process_period_col(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Function specifically built to process period field from MSW api.

    Args:
        df: DataFrame containing dictionary
        column: Column in DataFrame that contains period field, str
    """
    df[column] = df[column].apply(pd.Series)
    df[column] = df[column].apply(pd.Series)

    df = df.rename(columns={column: "period"})

    return df


def process_json(target_url: str, spot_name: str, longitude: int, latitude: int) -> pd.DataFrame:
    """Returns a DataFrame as read from MSW api with 2 new columns (spot & weekday).

    Args:
        target_url: The api target
        spot_name: Name of surf spot
        longitude: A surf spot's longitude
        latitude: A surf spot's latitude
    """
    df = pd.read_json(target_url)

    df["spot"] = spot_name
    df["longitude"] = longitude
    df["latitude"] = latitude
    df["time_now"] = dt.datetime.now()
    df["time_delta"] = (df["timestamp"] - df["time_now"])

    df = df[df["time_delta"] >= pd.Timedelta(0)]
    df = df.sort_values("time_delta")
    df = df.drop(["time_now", "time_delta"], axis=1)
    df = df.drop_duplicates(subset="spot")

    df = dict_to_series(df=df, column="wind")
    df = dict_to_series(df=df, column="swell")

    df = process_period_col(df=df, column="components")

    df = df.reset_index(drop=True)

    return df
