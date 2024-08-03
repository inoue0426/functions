import pandas as pd

def read_large_csv(file_path, chunksize=100000):
    """
    Function to read a large CSV file by chunks
    """
    chunks = pd.read_csv(file_path, chunksize=chunksize)
    df = pd.concat(chunks, ignore_index=True)
    return df