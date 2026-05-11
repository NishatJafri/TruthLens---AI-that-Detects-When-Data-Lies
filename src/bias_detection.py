import pandas as pd

def detect_bias(data, threshold=0.7):

    df = data.copy()

    categorical_cols = df.select_dtypes(include="object").columns

    bias_report = {}

    for col in categorical_cols:

        counts = df[col].value_counts(normalize=True, dropna=False)

        dominant_category = counts.idxmax()
        dominant_ratio = counts.max()

        if dominant_ratio >= threshold:
            bias_level = "High Bias"

        elif dominant_ratio >= 0.5:
            bias_level = "Moderate Bias"

        else:
            bias_level = "Low Bias"

        bias_report[col] = {

            "dominant_category": str(dominant_category),

            "dominant_ratio": round(float(dominant_ratio),3),

            "bias_level": bias_level,

            "distribution": counts.to_dict()
        }

    return bias_report