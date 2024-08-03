import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation(df, figsize=(12, 10)):
    """
    Function to visualize the correlation matrix of a dataframe as a heatmap
    """
    corr = df.corr()
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, center=0)
    plt.title("Correlation Heatmap")
    plt.show()
