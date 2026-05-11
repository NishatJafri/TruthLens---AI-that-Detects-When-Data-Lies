import pandas as pd
import numpy as np

def clean_data(data):

    df = data.copy()

    # remove duplicates
    df = df.drop_duplicates()

    # replace infinite values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    numeric_cols = df.select_dtypes(include=np.number).columns
    categorical_cols = df.select_dtypes(include="object").columns

    # fill numeric values with median
    for col in numeric_cols:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

    # fill categorical with mode
    for col in categorical_cols:

        mode_val = df[col].mode()

        if not mode_val.empty:
            df[col] = df[col].fillna(mode_val[0])
        else:
            df[col] = df[col].fillna("Unknown")

    return df