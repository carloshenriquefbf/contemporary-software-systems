import pandas as pd
import os

for filename in os.listdir('./final_results'):
    if filename.endswith('.csv'):
        filepath = os.path.join('./final_results', filename)
        df = pd.read_csv(filepath)
        df.drop_duplicates(subset=['link'], inplace=True)
        cleaned_filename = filename.replace('.csv', '_cleaned.csv')
        cleaned_filepath = os.path.join('./final_results', cleaned_filename)
        df.to_csv(cleaned_filepath, index=False)
        print(f"Cleaned DataFrame saved to {cleaned_filepath}")