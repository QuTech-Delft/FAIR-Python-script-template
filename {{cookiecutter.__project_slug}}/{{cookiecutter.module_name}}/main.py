from {{cookiecutter.module_name}}.processing import filter_outliers
import pandas as pd

INPUT_FILE_PATH = './example_input.csv'
OUTPUT_PATH = './output.csv'
THRESHOLD = 5
COLUMN_NAME = 'column_1'

try:
    data = pd.read_csv(INPUT_FILE_PATH)
except FileNotFoundError:
    print(f"File '{INPUT_FILE_PATH}' not found. Make sure the file exists.")
else:
    filtered_df = filter_outliers(data, COLUMN_NAME, THRESHOLD)
    filtered_df.to_csv(OUTPUT_PATH, index=False)
