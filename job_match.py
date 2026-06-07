job_roles = {

    "Python Developer": [
        "Python",
        "SQL",
        "Git",
        "GitHub",
        "Flask",
        "Django"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Data Analysis"
    ],

    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React"
    ],

    "Java Developer": [
        "Java",
        "SQL",
        "Git",
        "GitHub"
    ]
}


def calculate_job_match(role, skills):

    required_skills = job_roles[role]

    matched = []
    missing = []

    for skill in required_skills:

        if skill in skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int(
        (len(matched) / len(required_skills))
        * 100
    )

    return score, matched, missing