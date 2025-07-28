import sqlite3

def store_session_data(user_input, data, service, pitch):
    conn = sqlite3.connect('ai_recruitment_agent/db/log.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logs (input TEXT, data TEXT, service TEXT, pitch TEXT)")
    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?)", (user_input, str(data), service, pitch))
    conn.commit()
    conn.close()
