from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg2
import socket

app = Flask(__name__)
CORS(app)
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "testdb")
DB_USER = os.getenv("DB_USER", "testuser")
DB_PASS = os.getenv("DB_PASS")

DB_PASS_FILE = os.getenv("DB_PASS_FILE", "/run/secrets/db_password")
if not DB_PASS and os.path.exists(DB_PASS_FILE):
    with open(DB_PASS_FILE, "r") as f:
        DB_PASS = f.read().strip()


def get_db_message():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            dbname=DB_NAME,
        )
        cur = conn.cursor()
        cur.execute("SELECT message FROM greetings LIMIT 1;")
        row = cur.fetchone()
        conn.close()
        return row[0] if row else "No message in DB"
    except Exception as e:
        return f"DB error: {e}"


@app.route("/api/hello")
def hello():
    hostname = socket.gethostname()
    db_message = get_db_message()
    return jsonify({
        "backend": "Python Flask service",
        "hostname": hostname,
        "db_message": db_message
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
