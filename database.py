import sqlite3

# Connect to DB and create cursor to execute queries
conn = sqlite3.connect('./database/quizzes.db')
cursor = conn.cursor()
