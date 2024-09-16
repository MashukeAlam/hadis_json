from huggingface_hub import HfApi, create_repo
from datasets import DatasetDict

from datasets import Dataset
import pandas as pd

# Load your CSV file
df = pd.read_csv("hadith_data.csv")

# Convert the DataFrame into a Hugging Face Dataset object
dataset = Dataset.from_pandas(df)

# Save the dataset locally (optional)
dataset.save_to_disk("./hadith_dataset")


# Set the repository name
repo_name = "hadith_data"  # Change this to your desired repo name

# Create a new dataset repository
api = HfApi()
api.create_repo(repo_name, repo_type="dataset")

# Push the dataset to the repository
dataset.push_to_hub(repo_name)
