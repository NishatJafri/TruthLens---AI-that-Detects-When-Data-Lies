def calculate_truth_score(data):

    df = data.copy()

    total_rows = len(df)

    if total_rows == 0:
        return 0

    # anomaly penalty
    if "anomaly" in df.columns:
        anomalies = (df["anomaly"] == -1).sum()
    else:
        anomalies = 0

    anomaly_ratio = anomalies / total_rows

    # missing penalty
    missing = df.isnull().sum().sum()

    missing_ratio = missing / (total_rows * len(df.columns))

    # duplicate penalty
    duplicates = df.duplicated().sum()

    duplicate_ratio = duplicates / total_rows

    # final truth score
    penalty = anomaly_ratio + missing_ratio + duplicate_ratio

    truth_score = (1 - penalty) * 100

    return round(truth_score,2)