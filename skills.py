SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "react", "node.js", "data analysis",
    "aws", "docker", "flask", "django", "rest api"
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))