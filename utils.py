def highlight_matched_skills(skills, jd):
    return [skill for skill in skills if skill.lower() in jd.lower()]