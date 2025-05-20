import pandas as pd

def parse_logs(filepath):
    """
    Parses CIC-style CSV logs and returns a DataFrame with cleaned datetime columns.
    """
    df = pd.read_csv(filepath, low_memory=False)

    # Parse datetime fields if they exist
    for col in ['startDateTime', 'stopDateTime']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    return df
