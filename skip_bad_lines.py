import pandas as pd

def return_df_with_skip(PATH):
  return pd.read_csv(PATH, on_bad_lines='skip')
