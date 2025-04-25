# main file
import numpy as np
import pandas as pd
import spacy
from spacy import displacy

# Read data
df = pd.read_csv('C:/My Extra Things/Resume_Analysis/RESUME_ANALYSIS/resume.csv')

# This gives all the row indices of the DataFrame.
# Randomly shuffle the order of those indices and reorder the rows.
df = df.reindex(np.random.permutation(df.index))

# Create a copy of df and select only the first 1000 rows.
data = df.copy().iloc[:1000]

# Display the first 5 rows of the DataFrame data.
print(data.head())

# Load the SpaCy language model
nlp = spacy.load("en_core_web_sm")

# Render the named entities in the first resume.
sent = nlp(data["Resume_str"].iloc[0])
displacy.render(sent, style="ent", jupyter=True)

# try>:
# print(data.drop(columns=["Resume_str"]))
# print(data.drop(columns=["Resume_html"]))
print(data[["ID", "Category"]])