import pandas as pd

# Load the csv files
phishing_df = pd.read_csv('upload_data-to_db/phising_08012020_120000.csv')
predicted_df = pd.read_csv('predictions/prediction_file.csv')

# Ensure both dataframes have the result column
if 'Result' not in phishing_df.columns or 'Result' not in predicted_df.columns:
    raise ValueError("Both CSV files must contain a 'Result' column.")

# Standardize the 'Result' column in phishing_df: map -1 to 0 and 1 to 1
phishing_df['Result'] = phishing_df['Result'].map({-1: 0, 1: 1})

# Standardize the 'Result' column in predicted_df: map 'phising' to 0 and 'safe' to 1
predicted_df['Result'] = predicted_df['Result'].map({'phising': 0, 'safe': 1})

# Ensure both dataframes have the same number of rows for comparison
if len(phishing_df) != len(predicted_df):
    print("Warning: The number of rows in the original dataset and prediction file are different. Cannot accurately calculate accuracy.")
else:
    # Calculate number of matching values
    matching_values = (phishing_df['Result'] == predicted_df['Result']).sum()

    # Calculate total number of rows
    total_rows = len(phishing_df)

    print("Total Rows:", total_rows)
    print("Matching Values:", matching_values)

    # Calculate the accuracy score
    accuracy_score = matching_values / total_rows
    print(f"Accuracy score:{accuracy_score:.2f}")