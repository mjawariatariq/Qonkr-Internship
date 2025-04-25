# cleaner file
import pandas as pd
import re  # For regular expressions (used to clean text)
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')

data = pd.DataFrame({
    "Resume_str": ["Example resume text 1", "Example resume text 2"]
})

# Empty list to store the cleaned version of each resume.
clean = []

# Loop through each row in the DataFrame to clean resume text
for i in range(data.shape[0]):
    # Ye line resume se username, URLs, aur special characters hata deti hai.
    review = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', " ", data["Resume_str"].iloc[i])

    # Text ko chhoti alphabets mein convert karta hai aur har word ko list mein daal deta hai.
    review = review.lower().split()

    # Har word ka base form nikaala ja raha hai (lemmatization), aur common bekaar lafz (stopwords) remove ho rahe hain.
    lm = WordNetLemmatizer()
    review = [lm.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]

    # Saaf kiye gaye words ko wapas ek string mein jod ke clean list mein store karte hain.
    review = ' '.join(review)
    clean.append(review)  # Ensure to append the cleaned version to the clean list.

# Add cleaned resume and skills columns to DataFrame
data["Cleaned_Resume"] = clean
data["skills"] = data["Cleaned_Resume"].str.lower().str.split()
