# Skill extractor function ko import kar rahe hain
from skill_extractor import get_skills

jd_text = """
Looking for a HR Consultant.
"""

jd_skills = get_skills(jd_text)

import pandas as pd

data = pd.read_csv('resume.csv')

# Ab hum data ke har resume ko loop ke zariye process karenge
for i in range(data.shape[0]):
    # Har resume ka text "Resume_str" column se le rahe hain
    resume_text = data["Resume_str"].iloc[i]
    
    # Har resume ke skills extract kar rahe hain using `get_skills()`
    resume_skills = get_skills(resume_text)

    # Matched skills ko find kar rahe hain (common skills jo job description aur resume dono mein hain)
    matched = list(set(resume_skills) & set(jd_skills))
    
    # Missing skills ko find kar rahe hain (skills jo job description mein hain lekin resume mein nahi hain)
    missing = list(set(jd_skills) - set(resume_skills))
    
    # Match score calculate kar rahe hain (kitni skills match hui hain job description ke saath)
    score = len(matched) / len(jd_skills) * 100 if jd_skills else 0

    # Har resume ke liye matched skills, missing skills aur match score print kar rahe hain
    print(f"\nResume #{i+1}")
    print(f"Matched Skills: {matched}")
    print(f"Missing Skills: {missing}")
    print(f"Match Score: {score:.2f}%")
