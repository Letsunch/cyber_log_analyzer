import pandas as pd

def parse_logs(filepath):
    df = pd.read_csv(filepath, low_memory=False)
    df.columns = [col.strip() for col in df.columns]  # Clean headers
    return df
