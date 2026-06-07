skills_db = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Git",
    "GitHub",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Deep Learning",
    "Data Analysis",
    "Streamlit",
    "NLP",
    "Flask",
    "Django",
    "React",
    "Node.js",
    "MongoDB",
    "MySQL",
    "AWS",
    "Docker",
    "REST API"
]


def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills_db:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills