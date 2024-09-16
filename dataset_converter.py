from datasets import Dataset
import pandas as pd

# Load your CSV file
df = pd.read_csv("hadith_data.csv")

# Convert the DataFrame into a Hugging Face Dataset object
dataset = Dataset.from_pandas(df)

# Save the dataset locally (optional)
dataset.save_to_disk("./hadith_dataset")
