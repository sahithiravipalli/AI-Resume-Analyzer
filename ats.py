def calculate_ats_score(email, phone, skills, text):

    score = 0
    text = text.lower()

    if email != "Not Found":
        score += 10

    if phone != "Not Found":
        score += 10

    if "education" in text:
        score += 10

    if "project" in text:
        score += 15

    if "internship" in text:
        score += 15

    if "certification" in text or "certifications" in text:
        score += 10

    score += min(len(skills) * 2, 15)

    if "github" in text:
        score += 5

    if "linkedin" in text:
        score += 5

    words = len(text.split())

    if words >= 250:
        score += 10

    return score