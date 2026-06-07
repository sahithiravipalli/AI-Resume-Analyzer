import sqlite3

conn = sqlite3.connect(
    "resume_analysis.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    phone TEXT,
    ats_score INTEGER,
    role TEXT
)
""")

conn.commit()


def save_analysis(
    email,
    phone,
    ats_score,
    role
):

    cursor.execute(
        """
        INSERT INTO analysis
        (
            email,
            phone,
            ats_score,
            role
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            email,
            phone,
            ats_score,
            role
        )
    )

    conn.commit()