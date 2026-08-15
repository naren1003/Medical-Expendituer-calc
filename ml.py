import pandas as pd
medical_df = pd.read_csv('medical.csv')
print(medical_df)
print(medical_df.info())
print(medical_df.describe())
