import pandas as pd

def read_data(file: str) -> pd.DataFrame:
    data = pd.read_csv(file,
                       sep=",",
                       parse_dates=[0])
    
    # Strip whitespaces from the column names
    data.columns = [name.strip() for name in data.columns.values]

    return data


def process_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """
    Format and perform calculations on the Dataframe:
    1. The number of days passed
    2. The total reps of each exercise
    3. The total progress made (in %)
    """
    processed_data = raw_data.copy()
    
    # 1: Get the days elapsed from reference
    processed_data["days"] = (processed_data["Date"] - processed_data.loc[0, "Date"]).dt.days

    # 2-3: Compute the progress made
    processed_data["total_reps"] = processed_data.iloc[:, 1:].sum(axis=1) - processed_data['days']
    processed_data["progress"] = 100 * processed_data.loc[:, "total_reps"] / processed_data.loc[0, "total_reps"]

    return processed_data