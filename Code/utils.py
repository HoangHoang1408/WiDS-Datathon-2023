import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from feature_names import *

pd.options.display.max_columns = None
sns.set()


def df_info(df: pd.DataFrame):
    nan_count = df.isna().sum()
    df_info = pd.DataFrame(
        {
            "nan_count": nan_count,
            "nan_percent": np.round(nan_count * 100 / len(df), 4),
            "unique_count": df.nunique(),
            "dtype": df.dtypes,
        }
    )
    return df_info


def plot_line(
    df: pd.DataFrame, column_name: list[str], start_index: int = 0, end_index: int = 50
):
    plt.figure(figsize=(20, 8))
    for col in column_name:
        sns.lineplot(x=startdate, y=col, data=df.iloc[start_index:end_index], label=col)
    plt.xticks(rotation=90)
    plt.ylabel("Values")
    plt.xlabel("Date")
    plt.legend()
    plt.show()
