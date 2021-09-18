import sqlite3

# creates the database or connects to it
conn = sqlite3.connect('onboarding_modals.db')

# creates a cursor for sql commands
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS onboarding_modals (user_id TEXT, modal_text TEXT, user_action TEXT, ab_group TEXT)")

with open('onboarding_modals.txt', 'r') as f:
	data = [row.split('\t') for row in f.readlines()]

# inserts data into table
cur.executemany("INSERT INTO onboarding_modals (user_id, modal_text, user_action, ab_group) VALUES (?, ?, ?, ?);", data)

# runs commands
conn.commit()
# closes connection
conn.close()