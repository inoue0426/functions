def calculate_summary_stats(df, numeric_only=True):
    """
    データフレームの詳細な要約統計量を計算する関数
    """
    if numeric_only:
        df = df.select_dtypes(include=[np.number])
    
    summary = df.describe()
    summary.loc['skew'] = df.skew()
    summary.loc['kurtosis'] = df.kurtosis()
    summary.loc['median'] = df.median()
    summary.loc['mode'] = df.mode().iloc[0]
    summary.loc['range'] = df.max() - df.min()
    summary.loc['IQR'] = df.quantile(0.75) - df.quantile(0.25)
    
    return summary