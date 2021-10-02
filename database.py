import sqlite3

# Connect to DB and create cursor to execute queries
with sqlite3.connect('./database/quizzes.db') as conn:
    conn.row_factory = sqlite3.Row  # Upgrade row_factory
    cursor = conn.cursor()
