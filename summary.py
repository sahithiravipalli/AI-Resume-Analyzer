def generate_summary(skills):

    if skills:
        return (
            f"This resume demonstrates skills in "
            f"{', '.join(skills)}. "
            f"The candidate appears to have a technical background and relevant competencies for software-related roles."
        )

    return (
        "No significant technical skills were detected in the resume."
    )