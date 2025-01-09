import pandas as pd

def read_data(file: str) -> tuple[pd.DataFrame, tuple]:
    data = pd.read_csv(file,
                       sep=",",
                       parse_dates=[0])
    
    # Strip whitespaces from the column names
    data.columns = [name.strip() for name in data.columns.values]
    
    # Get the workout types from here
    omitted_columns = ('Date', 'days', 'total_reps', 'progress')
    workout_names = [column for column in data.columns.values if column not in omitted_columns]

    return data, workout_names


def process_data(raw_data: pd.DataFrame, columns: tuple) -> pd.DataFrame:
    """
    Format and perform calculations on the Dataframe:
    1. The number of days passed
    2. The total reps of each exercise
    3. The total progress made (in %)
    """
    processed_data = raw_data.copy()
    
    # Get the days elapsed from reference
    processed_data["days"] = (processed_data["Date"] - processed_data.loc[0, "Date"]).dt.days

    # Compute the progress made
    processed_data["total_reps"] = processed_data[columns].sum(axis='columns', numeric_only=True)
    processed_data["progress"] = 100 * processed_data.loc[:, "total_reps"] / processed_data.loc[0, "total_reps"]

    # print(processed_data)
    return processed_data