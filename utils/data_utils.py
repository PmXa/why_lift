import pandas as pd

def read_data(file: str) -> pd.DataFrame:
    data = pd.read_csv(file, parse_dates=["Date"])
    return data


def process_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """
    Format and perform calculations on the Dataframe:
    1. The number of days passed
    2. The total reps of each exercise
    3. The total progress made (in %)
    """
    processed_data = raw_data.copy()
    
    # Get the days elapsed from reference
    processed_data["days"] = (raw_data["Date"] - raw_data.loc[0, "Date"]).dt.days

    # Compute the progress made
    processed_data["total_reps"] = raw_data.iloc[:, 1:].sum(axis=1)
    processed_data["progress"] = 100 * processed_data.loc[:, "total_reps"] / processed_data.loc[0, "total_reps"]

    processed_data.to_csv('./dump_test.csv')
    return processed_data