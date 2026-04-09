from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

def detect_anomalies(data, contamination=0.1):

    df = data.copy()

    numeric_cols = df.select_dtypes(include=np.number)

    numeric_cols = numeric_cols.drop(
        columns=[c for c in numeric_cols.columns if "id" in c.lower()],
        errors="ignore"
    )

    if numeric_cols.shape[1] == 0:

        df["anomaly"] = 1
        df["anomaly_score"] = 0

        return df

    numeric_cols = numeric_cols.fillna(numeric_cols.median())

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(numeric_cols)

    model = IsolationForest(
        contamination=contamination,
        n_estimators=200,
        random_state=42
    )

    predictions = model.fit_predict(scaled_data)

    scores = model.decision_function(scaled_data)

    df["anomaly"] = predictions
    df["anomaly_score"] = scores

    return df
