import numpy as np

def explain_anomalies(data):

    explanations = []

    numeric_cols = data.select_dtypes(include=np.number).columns

    numeric_cols = [c for c in numeric_cols if c not in ["anomaly","anomaly_score"]]

    means = data[numeric_cols].mean()

    stds = data[numeric_cols].std().replace(0,1)

    anomalies = data[data["anomaly"] == -1]

    for index,row in anomalies.iterrows():

        reasons = []

        for col in numeric_cols:

            value = row[col]

            mean = means[col]

            std = stds[col]

            if abs(value - mean) > 3 * std:

                reasons.append(f"{col} value {value:.2f} deviates strongly from mean {mean:.2f}")

        explanations.append({

            "row": int(index),

            "reason": ", ".join(reasons) if reasons else "Unusual statistical pattern detected"
        })

    return explanations