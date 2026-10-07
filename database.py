"""
Database layer — SQLite via SQLAlchemy
Handles users, resume sessions, and analytics storage
"""

import sqlite3
import os
import bcrypt
import json
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "career_copilot.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create all tables if they don't exist."""
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        resume_text TEXT,
        ats_score INTEGER,
        job_match_data TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS interview_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        role TEXT,
        score INTEGER,
        questions_count INTEGER,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )""")

    conn.commit()
    conn.close()


def get_user(username: str):
    conn = get_conn()
    row = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    conn.close()
    return dict(row) if row else None


def create_user(username: str, email: str, password: str):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conn = get_conn()
    try:
        conn.execute("INSERT INTO users (username, email, password_hash) VALUES (?,?,?)",
                     (username, email, hashed))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def verify_password(password: str, hash_str: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode(), hash_str.encode())
    except Exception:
        return False


def save_session(user_id: int, resume_text: str, ats_score: int, job_match: dict):
    conn = get_conn()
    conn.execute(
        "INSERT INTO sessions (user_id, resume_text, ats_score, job_match_data) VALUES (?,?,?,?)",
        (user_id, resume_text, ats_score, json.dumps(job_match))
    )
    conn.commit()
    conn.close()


def get_user_sessions(user_id: int):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM sessions WHERE user_id=? ORDER BY created_at DESC LIMIT 10", (user_id,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def save_interview_log(user_id: int, role: str, score: int, count: int):
    conn = get_conn()
    conn.execute(
        "INSERT INTO interview_logs (user_id, role, score, questions_count) VALUES (?,?,?,?)",
        (user_id, role, score, count)
    )
    conn.commit()
    conn.close()


def get_interview_logs(user_id: int):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM interview_logs WHERE user_id=? ORDER BY created_at DESC LIMIT 20", (user_id,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
