import sys


def object_size(obj):
    """
    Function to return the memory usage of an object in MB
    """
    return sys.getsizeof(obj) / (1024 * 1024)


def dataframe_memory_usage(df):
    """
    Function to display the memory usage of each column in a dataframe
    """
    for col in df.columns:
        print(f"{col}: {object_size(df[col]):.2f} MB")
    print(f"Total: {object_size(df):.2f} MB")
