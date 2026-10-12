from dotenv import load_dotenv
load_dotenv(override=True)

import pandas as pd
import numpy as np
from src.utils.main_utils import MainUtils

# Load model locally (skip S3 download - use local file)
utils = MainUtils()
model = utils.load_object(file_path="artifacts/07_11_2026_06_23_19/model_trainer/trained_model/model.pkl")

# Create test input - 5 sample rows with 30 features
data = {
    'having_IP_Address': [1, -1, 1, -1, 1],
    'URL_Length': [-1, 1, -1, 1, -1],
    'Shortining_Service': [1, -1, 1, -1, 1],
    'having_At_Symbol': [-1, 1, -1, 1, -1],
    'double_slash_redirecting': [1, -1, 1, -1, 1],
    'Prefix_Suffix': [-1, 1, -1, 1, -1],
    'having_Sub_Domain': [1, -1, 1, -1, 1],
    'SSLfinal_State': [-1, 1, -1, 1, -1],
    'Domain_registeration_length': [1, -1, 1, -1, 1],
    'Favicon': [-1, 1, -1, 1, -1],
    'port': [1, -1, 1, -1, 1],
    'HTTPS_token': [-1, 1, -1, 1, -1],
    'Request_URL': [1, -1, 1, -1, 1],
    'URL_of_Anchor': [-1, 1, -1, 1, -1],
    'Links_in_tags': [1, -1, 1, -1, 1],
    'SFH': [-1, 1, -1, 1, -1],
    'Submitting_to_email': [1, -1, 1, -1, 1],
    'Abnormal_URL': [-1, 1, -1, 1, -1],
    'Redirect': [1, -1, 1, -1, 1],
    'on_mouseover': [-1, 1, -1, 1, -1],
    'RightClick': [1, -1, 1, -1, 1],
    'popUpWidnow': [-1, 1, -1, 1, -1],
    'Iframe': [1, -1, 1, -1, 1],
    'age_of_domain': [-1, 1, -1, 1, -1],
    'DNSRecord': [1, -1, 1, -1, 1],
    'web_traffic': [-1, 1, -1, 1, -1],
    'Page_Rank': [1, -1, 1, -1, 1],
    'Google_Index': [-1, 1, -1, 1, -1],
    'Links_pointing_to_page': [1, -1, 1, -1, 1],
    'Statistical_report': [-1, 1, -1, 1, -1]
}

df = pd.DataFrame(data)
print("Input shape:", df.shape)

# Predict
predictions = model.predict(df)

# Map back to labels
mapping = {0: 'phishing', 1: 'safe'}
results = [mapping[p] for p in predictions]

print("\nPredictions:")
for i, result in enumerate(results):
    print(f"  Row {i+1}: {result}")