def display_stats(df):
    """
    Function to display basic statistics of a dataframe
    """
    print(f"Shape of the dataframe: {df.shape}")
    print("\nData types of each column:")
    print(df.dtypes)
    print("\nBasic statistics of numerical columns:")
    print(df.describe())
    print("\nNumber of missing values:")
    print(df.isnull().sum())
