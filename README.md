# Hadith Dataset

This repository contains a dataset of Hadith collected from [Sunnah.com](https://sunnah.com). The dataset includes both English translations and references to the original Arabic texts, with links to the respective sources. The dataset was extracted using BeautifulSoup and is provided in CSV format for ease of use.

## Dataset Overview

- **Source**: [Sunnah.com](https://sunnah.com)
- **Language**: English (with references to Arabic texts)
- **Format**: CSV
- **Use cases**: This dataset can be used for natural language processing (NLP) tasks, religious studies, text classification, and text analysis.

### CSV Structure

The dataset contains the following columns:

- **narrator**: The name of the narrator of the Hadith (if available).
- **english_text**: The English translation of the Hadith text.
- **hadith_link**: A link to the full Hadith on Sunnah.com.
- **reference**: The reference information for the Hadith (e.g., book, volume, hadith number).

### Example Entry

| narrator          | english_text                                                       | hadith_link        | reference               |
|-------------------|---------------------------------------------------------------------|--------------------|-------------------------|
| Abu Huraira       | "The Prophet said, 'The best of charity is that which is given ...'" | /bukhari:3         | Sahih al-Bukhari 3       |

