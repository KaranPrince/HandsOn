from flask import Flask, jsonify
import psycopg2
import os
import socket

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "testdb")
DB_USER = os.getenv("DB_USER", "testuser")
DB_PASS = os.getenv("DB_PASS", "testpass")

def get_db_message():
    try:
        # connect with short timeout to avoid hanging while DB comes up
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME,
            user=DB_USER, password=DB_PASS,
            connect_timeout=3
        )
        cur = conn.cursor()
        cur.execute("SELECT message FROM hello LIMIT 1;")
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row[0] if row else "No data"
    except Exception as e:
        # return a concise error (helps debugging without noisy tracebacks to frontend)
        return f"DB error: {str(e)}"

@app.route("/api/hello")
def hello():
    return jsonify({
        "backend": "Python Flask service",
        "hostname": socket.gethostname(),
        "db_message": get_db_message()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
