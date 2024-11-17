from huggingface_hub import HfApi, create_repo
from datasets import DatasetDict

from datasets import Dataset
import pandas as pd

df = pd.read_csv("hadith_data.csv")

dataset = Dataset.from_pandas(df)

dataset.save_to_disk("./hadith_dataset")


repo_name = "hadith_data"  # Change this to your desired repo name

api = HfApi()
# api.create_repo(repo_name, repo_type="dataset")

dataset.push_to_hub(repo_name)
