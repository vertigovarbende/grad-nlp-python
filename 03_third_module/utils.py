import pandas as pd

def load_dataset(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    return df