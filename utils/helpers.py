import pandas as pd
import numpy as np
import os


# Load dataset safely
def load_data(file):

    try:
        data = pd.read_csv(file)
        return data

    except Exception as e:

        raise ValueError(f"Error loading dataset: {e}")


# Export processed dataset for PowerBI or external tools
def export_for_powerbi(data, filename="truthlens_dataset.csv"):

    os.makedirs("output", exist_ok=True)

    filepath = os.path.join("output", filename)

    data.to_csv(filepath, index=False)

    return filepath


# Detect numeric columns excluding ID fields
def get_numeric_columns(data):

    numeric_cols = data.select_dtypes(include=np.number).columns

    numeric_cols = [c for c in numeric_cols if "id" not in c.lower()]

    return numeric_cols


# Generate dataset summary
def dataset_summary(data):

    summary = {

        "rows": data.shape[0],

        "columns": data.shape[1],

        "missing_values": int(data.isnull().sum().sum()),

        "duplicates": int(data.duplicated().sum()),

        "numeric_columns": len(data.select_dtypes(include=np.number).columns),

        "categorical_columns": len(data.select_dtypes(include="object").columns)
    }

    return summary


# Identify columns with high missing values
def missing_value_report(data, threshold=20):

    missing = data.isnull().sum()

    missing_percent = (missing / len(data)) * 100

    report = pd.DataFrame({

        "Column": data.columns,

        "Missing Count": missing.values,

        "Missing %": missing_percent.values

    })

    problem_columns = report[report["Missing %"] > threshold]

    return report, problem_columns


# Detect duplicate rows
def duplicate_report(data):

    duplicates = data[data.duplicated()]

    count = duplicates.shape[0]

    return count, duplicates


# Get dataset statistics
def dataset_statistics(data):

    stats = data.describe(include="all")

    return stats


# Validate dataset before analysis
def validate_dataset(data):

    issues = []

    if data.shape[0] == 0:

        issues.append("Dataset contains no rows.")

    if data.shape[1] == 0:

        issues.append("Dataset contains no columns.")

    missing = data.isnull().sum().sum()

    if missing > 0:

        issues.append(f"Dataset contains {missing} missing values.")

    duplicates = data.duplicated().sum()

    if duplicates > 0:

        issues.append(f"Dataset contains {duplicates} duplicate rows.")

    return issues