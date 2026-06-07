def generate_suggestions(text, skills):

    suggestions = []

    text = text.lower()

    if "github" not in text:
        suggestions.append("Add GitHub profile")

    if "linkedin" not in text:
        suggestions.append("Add LinkedIn profile")

    if "certification" not in text and "certifications" not in text:
        suggestions.append("Add Certifications")

    if "internship" not in text:
        suggestions.append("Add Internship Experience")

    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    return suggestions